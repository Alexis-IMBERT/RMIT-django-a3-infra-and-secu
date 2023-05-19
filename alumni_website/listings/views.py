""" Methods for the view traitment """
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout, forms

# from django.contrib import messages

from .forms import DiplomaNumberForm
from .forms import UserRegisterForm

from .models import DiplomaNumber

from .utils import get_current_year, generate_diploma_number


def get_user(request) -> User:
    """Return a user"""
    return User.objects.get(id=request.session["_auth_user_id"])


def hello(request):
    # alumnis = Alumni.objects.all()
    user = User.objects.all()
    return render(request, "listings/hello.html", {"alumnis": user})


def home(request):
    return render(
        request,
        "listings/home.html",
        {
            "title": "Website With Login & Registration Form Remitly",
        },
    )


def logout_view(request):
    logout(request)
    return redirect("home")


def login_view(request):
    if request.method == "POST":
        form = forms.AuthenticationForm(request=request)

        email = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return redirect("home")
            else:
                # Return a 'disabled account' error message
                ...
        else:
            # Return an 'invalid login' error message.
            ...
    else:
        form = forms.AuthenticationForm()

    return render(request, "listings/login.html", {"form": form})


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password1")
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, "listings/register.html", {"form": form})


@login_required()
def add_diploma(request):
    if request.method == "POST":
        form = DiplomaNumberForm(request.POST)
        if form.is_valid():
            year = request.POST.get("year")
            programe_name = request.POST.get("programe_name")
            user = get_user(request=request)
            diploma_number = generate_diploma_number(year)

            diplome = DiplomaNumber(
                diploma_number=diploma_number,
                user=user,
                year=year,
                programe_name=programe_name,
            )
            diplome.save()
            return redirect("info_diploma")
    else:
        year = get_current_year()
        values = {
            "year": year,
        }
        form = DiplomaNumberForm(values)

    return render(request, "listings/diploma-add.html", {"form": form})


@login_required()
def info_diploma(request):
    user = get_user(request=request)
    print(user.first_name)
    # diplomes = DiplomaNumber.objects.filter(username=user)
    diplomes = DiplomaNumber.objects.all()
    print(diplomes)
    return render(request, "listings/diploma-info.html", {"diplomes": diplomes})


def check_diploma(request):
    return render(request, "listings/diploma-check.html", {})


def terms_and_conditions(request):
    return render(
        request,
        "listings/terms_and_conditions.html",
        {
            "title": "Terms and Conditions",
        },
    )


def contact(request):
    return render(request, "listings/contact.html")


def service(request):
    return render(request, "listings/service.html")
