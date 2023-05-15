""" Creation of class forms of the app """
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """ Class for the registration form """
    first_name = forms.CharField(label='First Name', strip=True, required=True)
    last_name = forms.CharField(label='Last Name', strip=True, required=True)
    username = forms.EmailField(label='Email', required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'password1', 'password2')


class DiplomaNumberForm():
    pass
