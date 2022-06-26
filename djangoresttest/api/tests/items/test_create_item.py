from django.contrib.auth.models import User
from django.http import HttpResponse
from django.test import Client, TestCase

from djangoresttest.api.schemas.auth_schemas import LoginInSchema
from djangoresttest.api.services.auth_service import authenticate_user


class CreateItemTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user1", email="user1@user.com", password="Secret1234!")
        self.token = authenticate_user(LoginInSchema(username="user1", password="Secret1234!"))

    def test_create_item(self):
        c = Client()
        r: HttpResponse = c.post(
            "/api/v1/items/",
            {"name": "item_test", "description": "description_test", "attack": 5, "defense": 5, "magic": 5},
            content_type="application/json",
            HTTP_ACCEPT="application/json",
            HTTP_AUTHORIZATION=f"JWT {self.token}",
        )
        self.assertEqual(r.status_code, 200)

    def test_create_item_fail(self):
        c = Client()
        r: HttpResponse = c.post(
            "/api/v1/items/",
            {"name": "item_test", "description": "description_test", "attack": 5, "defense": 5, "magic": -32},
            content_type="application/json",
            HTTP_ACCEPT="application/json",
            HTTP_AUTHORIZATION=f"JWT {self.token}",
        )
        self.assertEqual(r.status_code, 422)
