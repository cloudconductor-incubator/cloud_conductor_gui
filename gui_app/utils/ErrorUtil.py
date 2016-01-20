from django import forms
from django.core.exceptions import ValidationError


class ApiError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)