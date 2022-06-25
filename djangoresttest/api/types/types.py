from typing import TypeVar

from django.contrib.auth.models import User
from django.http import HttpRequest

T = TypeVar("T")


class AuthHttpRequest(HttpRequest):
    auth: User
