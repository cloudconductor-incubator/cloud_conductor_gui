import re
from collections import namedtuple
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import django.contrib.auth as auth


def valiCheck(form):

    errors = form.errors.as_data()
    msg = ""
    for e in errors:
        msg = errors[e][0].messages[0]
        break
    return msg
