# -*- coding: utf-8 -*-
from django import forms


class loginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=64, min_length=8)
    rePassword = forms.CharField(
        max_length=64, min_length=8, widget=forms.PasswordInput, required=False)

    def clean_email(self):
        email = self.cleaned_data['email']


class projectForm(forms.Form):
    auth_token = forms.CharField()
    id = forms.IntegerField(required=False)
    name = forms.CharField(max_length=500)
    description = forms.CharField(required=False, max_length=500)


class cloudForm(forms.Form):
    auth_token = forms.CharField()
    id = forms.IntegerField(required=False)
    project_id = forms.CharField()
    name = forms.CharField(max_length=500)
    type = forms.CharField(max_length=500)
    key = forms.CharField(max_length=500)
    secret = forms.CharField(max_length=500)
    entry_point = forms.CharField(max_length=500)
    description = forms.CharField(required=False, max_length=500)
    tenant_name = forms.CharField(required=False, max_length=500)


class baseImageForm(forms.Form):
    auth_token = forms.CharField()
    id = forms.IntegerField(required=False)
    project_id = forms.CharField(required=False)
    cloud_id = forms.CharField()
    ssh_username = forms.CharField(max_length=500)
    source_image = forms.CharField(max_length=500)
    os = forms.CharField(required=False, max_length=500)


class systemForm(forms.Form):
    auth_token = forms.CharField()
    id = forms.IntegerField(required=False)
    project_id = forms.CharField(required=False)
    name = forms.CharField(required=False)
    description = forms.CharField(max_length=128)
    domain = forms.CharField()


class environmentForm(forms.Form):
    auth_token = forms.CharField()
    id = forms.IntegerField(required=False)
    project_id = forms.CharField(required=False)
    system_id = forms.CharField()
    blueprint_id = forms.CharField()
    name = forms.CharField()
    description = forms.CharField(required=False)
    template_parameters = forms.CharField(required=False)
    user_attributes = forms.CharField(required=False)
    candidates_attributes = forms.CharField(max_length=128)


class applicationForm(forms.Form):
    auth_token = forms.CharField()
    id = forms.IntegerField(required=False)
    project_id = forms.CharField(required=False)
    system_id = forms.CharField()
    name = forms.CharField()
    description = forms.CharField(required=False)
    domain = forms.CharField(required=False)


class blueprintForm(forms.Form):
    auth_token = forms.CharField()
    id = forms.IntegerField(required=False)
    project_id = forms.CharField(required=False)
    name = forms.CharField()
    description = forms.CharField(required=False)
    patterns_attributes = forms.CharField(required=False)


class patternForm(forms.Form):
    auth_token = forms.CharField()
    id = forms.IntegerField(required=False)
    project_id = forms.CharField(required=False)
    name = forms.CharField()
    protocol = forms.CharField(required=False)
    type = forms.CharField(required=False)
    pattern_url = forms.CharField(required=False)
    secret_key = forms.CharField(required=False)
    revision = forms.CharField(required=False)
    parameters = forms.CharField(required=False)
    roles = forms.CharField(required=False)
