from django.contrib.auth.models import User
from django.http import HttpResponse
from django.test import Client, TestCase

from djangoresttest.api.schemas.auth_schemas import LoginInSchema
from djangoresttest.api.services.auth_service import authenticate_user


class RequestItemTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user1", email="user1@user.com", password="Secret1234!")
        self.token = authenticate_user(LoginInSchema(username="user1", password="Secret1234!"))

    def test_request_items(self):
        c = Client()
        r: HttpResponse = c.get(
            "/api/v1/items/",
            content_type="application/json",
            HTTP_ACCEPT="application/json",
            HTTP_AUTHORIZATION=f"JWT {self.token}",
        )
        self.assertEqual(r.status_code, 200)

    def test_request_items_fail(self):
        c = Client()
        r: HttpResponse = c.get(
            "/api/v1/items/",
            content_type="application/json",
            HTTP_ACCEPT="application/json",
        )
        self.assertEqual(r.status_code, 401)
