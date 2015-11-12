# -*- coding: utf-8 -*-
from django import forms

class t_projectForm(forms.Form):
    id = forms.IntegerField(required=False)
    name = forms.CharField(max_length=64)
    description = forms.CharField(required=False, max_length=128)
    created_at = forms.CharField(required=False)
    created_at = forms.CharField(required=False)

    def clean_name(self):
        name = self.cleaned_data['name']

        if len(name) < 3:
            raise forms.ValidationError(u'3 len')
        return name

class loginForm(forms.Form):
    id = forms.IntegerField()
    email = forms.EmailField()
    account = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)
    rePassword = forms.CharField(max_length=64)

class cloudForm(forms.Form):
    id = forms.IntegerField(required=False)
    project_id = forms.IntegerField(required=False)
    name = forms.CharField()
    description = forms.CharField(required=False, max_length=100)
    type = forms.CharField(required=False)
    entry_point = forms.CharField(required=False)
    key = forms.CharField(required=False)
    secret = forms.CharField(required=False)
    tenant_name = forms.CharField(required=False)

class baseImageForm(forms.Form):
    id = forms.IntegerField(required=False)
    cloud_id = forms.IntegerField(required=False)
    os = forms.CharField()
    source_image = forms.CharField(required=False, max_length=100)
    ssh_username = forms.CharField(required=False)
    created_at = forms.CharField(required=False)
    updated_at = forms.CharField(required=False)

