# -*- coding: utf-8 -*-
import cgi
from django import forms
from .enum.MessageCode import Error


class loginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=64, min_length=8)
    rePassword = forms.CharField(
        max_length=500, min_length=8, widget=forms.PasswordInput, required=False)


class projectForm(forms.Form):
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
    id = forms.IntegerField(required=False)
    ssh_username = forms.CharField(max_length=500)
    source_image = forms.CharField(max_length=500)
    os = forms.CharField(required=False, max_length=500)


class systemForm(forms.Form):
    id = forms.IntegerField(required=False)
    name = forms.CharField(max_length=500)
    description = forms.CharField(required=False, max_length=500)
    domain = forms.CharField(required=False, max_length=500)
    environment = forms.CharField(required=False, max_length=500)


class systemSelectForm(forms.Form):
    id = forms.CharField()


class environmentSelectForm(forms.Form):
    id = forms.CharField()


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

    def clean(self):
        candidates_attributes_1 = self.cleaned_data.get('candidates_attributes_1', None)
        candidates_attributes_2 = self.cleaned_data.get('candidates_attributes_2', None)
        candidates_attributes_3 = self.cleaned_data.get('candidates_attributes_3', None)

        if candidates_attributes_2:
            if candidates_attributes_1 == candidates_attributes_2:
                raise forms.ValidationError(Error.DuplicationCloud.value)

        if candidates_attributes_3:
            if candidates_attributes_2 == candidates_attributes_3:
                raise forms.ValidationError(Error.DuplicationCloud.value)

            if candidates_attributes_1 == candidates_attributes_3:
                raise forms.ValidationError(Error.DuplicationCloud.value)

        return self.cleaned_data


class w_environmentForm(forms.Form):
    id = forms.IntegerField(required=False)
    blueprint_id = forms.CharField()
    version = forms.CharField(required=False)
    name = forms.CharField(max_length=500)
    description = forms.CharField(required=False, max_length=500)
    template_parameters = forms.CharField(required=False, max_length=500)
    user_attributes = forms.CharField(required=False, max_length=500)
    candidates_attributes_1 = forms.CharField(max_length=500)
    candidates_attributes_2 = forms.CharField(required=False, max_length=500)
    candidates_attributes_3 = forms.CharField(required=False, max_length=500)

    def clean(self):
        candidates_attributes_1 = self.cleaned_data.get('candidates_attributes_1', None)
        candidates_attributes_2 = self.cleaned_data.get('candidates_attributes_2', None)
        candidates_attributes_3 = self.cleaned_data.get('candidates_attributes_3', None)

        if candidates_attributes_2:
            if candidates_attributes_1 == candidates_attributes_2:
                raise forms.ValidationError(Error.DuplicationCloud.value)

        if candidates_attributes_3:
            if candidates_attributes_2 == candidates_attributes_3:
                raise forms.ValidationError(Error.DuplicationCloud.value)

            if candidates_attributes_1 == candidates_attributes_3:
                raise forms.ValidationError(Error.DuplicationCloud.value)

        return self.cleaned_data


class environmentSelectForm(forms.Form):
    id = forms.CharField()


class applicationForm(forms.Form):
    auth_token = forms.CharField()
    id = forms.IntegerField(required=False)
    project_id = forms.CharField(required=False)
    system_id = forms.CharField()
    name = forms.CharField(max_length=500)
    description = forms.CharField(required=False, max_length=500)
    domain = forms.CharField(required=False, max_length=500)


class w_applicationForm(forms.Form):
    name = forms.CharField(max_length=500)
    description = forms.CharField(required=False, max_length=500)
    domain = forms.CharField(required=False, max_length=500)
    url = forms.CharField(max_length=500)
    type = forms.CharField(required=False, max_length=500)
    protocol = forms.CharField(required=False, max_length=500)
    revision = forms.CharField(required=False, max_length=500)
    pre_deploy = forms.CharField(required=False, max_length=500)
    post_deploy = forms.CharField(required=False, max_length=500)
    parameters = forms.CharField(required=False, max_length=500)


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
        repassword = self.cleaned_data['repassword']
        if self.cleaned_data['password'] != self.cleaned_data['repassword']:
            raise forms.ValidationError(Error.PasswordMismatch.value)

        return repassword

class roleForm(forms.Form):
    name = forms.CharField(max_length=500)
    description = forms.CharField(required=False, max_length=500)

