from django import forms
from django.core import validators
from store.models import Customer
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password')

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('confirm_password','age')
        widgets = {
            'confirm_password':forms.PasswordInput()
        }

