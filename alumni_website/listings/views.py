""" Methods for the view traitment """
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout, forms
from django.contrib import messages

from .forms import DiplomaNumberForm
from .forms import UserRegisterForm


def hello(request):
    # alumnis = Alumni.objects.all()
    user = User.objects.all()
    return render(request, "listings/hello.html", {"alumnis": user})


def home(request):
    return render(request, "listings/home.html", {
        "title": "Website With Login & Registration Form Remitly",
    })


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(request=request)

        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return redirect('home')
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
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password1')
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, "listings/register.html", {'form': form})


@login_required(login_url='/login')
def set_information(request):
    return redirect('url login')


def diploma_number(request):
    form = DiplomaNumberForm()
    return render(request, "listings/diploma_number.html",{'form',form})


def terms_and_conditions(request):
    return render(request, "listings/terms_and_conditions.html", {
        "title": "Terms and Conditions",
    })


def service(request):
    return render(request, "listings/service.html")
