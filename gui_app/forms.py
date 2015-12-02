# -*- coding: utf-8 -*-
from django import forms

class t_projectForm(forms.Form):
    id = forms.IntegerField(required=False)
    name = forms.CharField(max_length=64)
    description = forms.CharField(required=False, max_length=128)

    def clean_name(self):
        name = self.cleaned_data['name']

        if len(name) < 3:
            raise forms.ValidationError(u'3 len')
        return name

class loginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=64, min_length=8)
    rePassword = forms.CharField(max_length=64, min_length=8, widget=forms.PasswordInput, required=False)

    def clean_email(self):
        email = self.cleaned_data['email']

        if len(email) < 6:
            raise forms.ValidationError(u'Please enter at least 6 characters.')
        return email

class cloudForm(forms.Form):
    id = forms.IntegerField(required=False)
    project_id = forms.CharField()
    name = forms.CharField()
    type = forms.CharField()
    key = forms.CharField()
    secret = forms.CharField()
    entry_point = forms.CharField()
    description = forms.CharField(required=False, max_length=128)
    tenant_name = forms.CharField(required=False)

class systemForm(forms.Form):
    id = forms.IntegerField(required=False)
    project_id = forms.CharField(required=False)
    name = forms.CharField(required=False)
    description = forms.CharField(max_length=128)
    domain = forms.CharField()

class environmentForm(forms.Form):
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
    id = forms.IntegerField(required=False)
    project_id = forms.CharField(required=False)
    system_id = forms.CharField()
    name = forms.CharField()
    description = forms.CharField(required=False)
    domain = forms.CharField(required=False)

class blueprintForm(forms.Form):
    id = forms.IntegerField(required=False)
    project_id = forms.CharField(required=False)
    name = forms.CharField()
    description = forms.CharField(required=False)
    patterns_attributes = forms.CharField(required=False)

class patternForm(forms.Form):
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

class baseImageForm(forms.Form):
    id = forms.IntegerField(required=False)
    project_id = forms.CharField(required=False)
    cloud_id = forms.CharField()
    ssh_username = forms.CharField()
    source_image = forms.CharField(max_length=100)
    os = forms.CharField()


