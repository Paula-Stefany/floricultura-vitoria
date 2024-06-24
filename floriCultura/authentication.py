from typing import Any
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import check_password
from django.http import HttpRequest
from .models import Client


class ClientBackend(BaseBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            client = Client.objects.get(email=email)
            if client and check_password(password, client.password):
                return client
        except Client.DoesNotExist:
            return None 
    def get_user(self, user_id):

        try:
            return Client.objects.get(pk=user_id)
        except Client.DoesNotExist:
            return None 
