# -*- coding: utf-8 -*-
import cgi
from django import forms


class loginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=64, min_length=8)
    rePassword = forms.CharField(
        max_length=500, min_length=8, widget=forms.PasswordInput, required=False)


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
    project_id = forms.CharField(required=False)
    auth_token = forms.CharField()
#     cloud_id = forms.CharField()
    id = forms.IntegerField(required=False)
    ssh_username = forms.CharField(max_length=500)
    source_image = forms.CharField(max_length=500)
    os = forms.CharField(required=False, max_length=500)


class systemForm(forms.Form):
    auth_token = forms.CharField()
    id = forms.IntegerField(required=False)
    project_id = forms.CharField(required=False)
    name = forms.CharField(max_length=500)
    description = forms.CharField(required=False, max_length=500)
    domain = forms.CharField(required=False, max_length=500)
    environment = forms.CharField(required=False, max_length=500)


class environmentForm(forms.Form):
    auth_token = forms.CharField()
    id = forms.IntegerField(required=False)
    project_id = forms.CharField(required=False)
    system_id = forms.CharField()
    blueprint_id = forms.CharField()
    version = forms.CharField(required=False)
    name = forms.CharField(max_length=500)
    description = forms.CharField(required=False, max_length=500)
    template_parameters = forms.CharField(required=False, max_length=500)
    user_attributes = forms.CharField(required=False, max_length=500)
    candidates_attributes_1 = forms.CharField(max_length=500)
    candidates_attributes_2 = forms.CharField(required=False, max_length=500)
    candidates_attributes_3 = forms.CharField(required=False, max_length=500)

class applicationForm(forms.Form):
    auth_token = forms.CharField()
    id = forms.IntegerField(required=False)
    project_id = forms.CharField(required=False)
    system_id = forms.CharField()
    name = forms.CharField(max_length=500)
    description = forms.CharField(required=False, max_length=500)
    domain = forms.CharField(required=False, max_length=500)


class blueprintForm(forms.Form):
    auth_token = forms.CharField()
    id = forms.IntegerField(required=False)
    project_id = forms.CharField(required=False)
    name = forms.CharField(max_length=500)
    description = forms.CharField(required=False, max_length=500)
    patterns_attributes = forms.CharField(required=False, max_length=500)


class patternForm(forms.Form):
    auth_token = forms.CharField()
    project_id = forms.CharField()
    url = forms.URLField(max_length=500)
    revision = forms.CharField(required=False, max_length=500)


class accountForm(forms.Form):
    auth_token = forms.CharField()
    email = forms.EmailField(max_length=500)
    name = forms.CharField(max_length=500)
    password = forms.CharField(max_length=500)
    repassword = forms.CharField(max_length=500)
    admin = forms.CharField(max_length=500)
    role = forms.CharField(max_length=500)

    def clean_repassword(self):
        if self.cleaned_data['password'] != self.cleaned_data['repassword']:
            raise forms.ValidationError(u"Passwords do not match")
