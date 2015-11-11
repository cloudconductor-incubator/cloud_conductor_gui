# -*- coding: utf-8 -*-
from django import forms

class t_projectForm(forms.Form):
    id = forms.IntegerField(required=False)
    name = forms.CharField()
    description = forms.CharField(required=False, max_length=100)
    created_at = forms.CharField(required=False)
    created_at = forms.CharField(required=False)

    def clean_t_projectForm(self):
          description = self.cleaned_data['description']
          if(description.find('<') != -1 or description.find('>') != -1):
              raise forms.ValidationError("error")
          return description

class loginForm(forms.Form):
    id = forms.IntegerField()
    email = forms.EmailField()
    account = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)
    rePassword = forms.CharField(max_length=64)

class cloudForm(forms.Form):
    id = forms.IntegerField()
    project_id = forms.IntegerField()
    name = forms.CharField()
    description = forms.CharField(required=False, max_length=100)
    type = forms.CharField()
    entry_point = forms.CharField()
    key = forms.CharField()
    secret = forms.CharField()
    tenant_name = forms.CharField(required=False)
