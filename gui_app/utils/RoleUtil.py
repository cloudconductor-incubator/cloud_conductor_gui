import re
from collections import namedtuple
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import django.contrib.auth as auth
import json
import requests


class UserParameters(namedtuple("User", ["email", "password", "password_confirm"])):
    def username(self):
        return self.email.split("@")[0]

    @classmethod
    def create(cls, params):
        p = [params[f] for f in cls._fields]
        return UserParameters(*p)

