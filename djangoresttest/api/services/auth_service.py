from calendar import timegm
from datetime import datetime
from typing import Optional

from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http.request import HttpRequest
from ninja.security import APIKeyHeader
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_decode_handler

from djangoresttest.api.schemas.auth_schemas import LoginInSchema, UserDataSchema
from djangoresttest.api.types.types import AuthHttpRequest
from djangoresttest.api.utils.exceptions import BaseException


def authenticate_user(user_data: LoginInSchema) -> str:
    user = User.objects.filter(username=user_data.username).first()
    if not user:
        raise BaseException("Wrong username or password.", 400, False)
    if not user.is_active:
        raise BaseException("Please, check your email to activate your account.", 412, False)
    if not check_password(user_data.password, user.password):
        raise BaseException("Wrong username or password.", 400, False)
    return get_token_jwt(user)


def jwt_payload_handler(user: User):
    payload = {
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "exp": datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
    }
    if api_settings.JWT_ALLOW_REFRESH:
        payload["orig_iat"] = timegm(datetime.utcnow().utctimetuple())
    if api_settings.JWT_AUDIENCE is not None:
        payload["aud"] = api_settings.JWT_AUDIENCE
    if api_settings.JWT_ISSUER is not None:
        payload["iss"] = api_settings.JWT_ISSUER
    return payload


def get_token_jwt(user: User):
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token


def get_logged_user(request: AuthHttpRequest) -> UserDataSchema:
    user: User = User.objects.get(id=request.auth.id)
    return UserDataSchema(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name or None,
    )


class ApiKey(APIKeyHeader):
    param_name = "Authorization"

    def authenticate(self, request: HttpRequest, key: Optional[str]):
        user = None
        if not key:
            raise BaseException("Unauthorized", "401")
        try:
            if settings.DEBUG and " " not in key:
                keyword = "JWT"
            else:
                keyword, key = key.split()
            if keyword != "JWT":
                raise Exception()
            payload = jwt_decode_handler(key)
            auth = BaseJSONWebTokenAuthentication()
            user = auth.authenticate_credentials(payload)
        except Exception:
            raise BaseException("Auth error.", "500")
        return user


api_key = ApiKey()
