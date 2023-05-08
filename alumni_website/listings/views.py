# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from listings.models import Alumni
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


def hello(request):
    # alumnis = Alumni.objects.all()
    user = User.objects.all()
    return render(request, "listings/hello.html", {"alumnis": user})


def home(request):
    return render(request, "listings/home.html")


def login_view(request):
    return render(request, "listings/login.html")


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, "listings/register.html", {'form': form})


@login_required(login_url='/login')
def set_information(request):
    return redirect('url login')


def diploma_number(request):
    return render(request, "listings/diploma_number.html")
