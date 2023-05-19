""" Creation of class forms of the app """
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import DiplomaNumber
from .utils import get_current_year


class UserRegisterForm(UserCreationForm):
    """Class for the registration form"""

    first_name = forms.CharField(
        label="First Name",
        strip=True,
        required=True,
    )
    last_name = forms.CharField(label="Last Name", strip=True, required=True)
    username = forms.EmailField(label="Email", required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")


class DiplomaNumberForm(ModelForm):
    """Form class for add a diploma number"""

    class Meta:
        model = DiplomaNumber
        fields = ("year", "programe_name")


class CheckDiplomaNumberForm(forms.Form):
    """Form to check the validity of a diploma number and it's"""

    diploma_number = forms.CharField(
        label="Diploma number", max_length=7, min_length=7, strip=True, required=True
    )
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")

    class Meta:
        fields = ("diploma_number", "username")

    class NumberDoesNotExist(Exception):
        pass

    class NameDoesNotMatch(Exception):
        pass

    def check(self) -> bool:
        form_number = self.cleaned_data["diploma_number"]
        form_first_name = self.cleaned_data["first_name"]
        form_last_name = self.cleaned_data["last_name"]
        try:
            diploma = DiplomaNumber.objects.get(pk=form_number)
        except DiplomaNumber.DoesNotExist as exc:
            raise self.NumberDoesNotExist() from exc

        diploma_first_name = diploma.user.first_name
        diploma_last_name = diploma.user.last_name

        if form_first_name != diploma_first_name or form_last_name != diploma_last_name:
            return self.NameDoesNotMatch()

        return True
