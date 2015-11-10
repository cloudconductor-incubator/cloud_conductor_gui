# -*- coding: utf-8 -*-
from django import forms

class t_projectForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField()
    description = forms.CharField(max_length=100)
    created_at = forms.CharField()
    created_at = forms.CharField()
    widget=forms.TextInput()

class loginForm(forms.Form):
    id = forms.IntegerField()
    email = forms.EmailField()
    account = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)
    rePassword = forms.CharField(max_length=64)
