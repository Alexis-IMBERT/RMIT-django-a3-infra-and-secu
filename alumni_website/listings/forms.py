from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name',strip=True)
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email address')
    student_id = forms.CharField(label="Student ID",min_length=8,max_length=8,strip=True)
    programe_name = forms.CharField(label="Program Name")
    year_graduation = forms.DateField(label="Year of graduation")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email')
