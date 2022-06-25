from typing import Optional

from ninja import Schema


class LoginInSchema(Schema):
    username: str
    password: str


class TokenDataSchema(Schema):
    token: str


class UserDataSchema(Schema):
    email: str
    first_name: str
    last_name: Optional[str] = ""
    password: Optional[str] = None
