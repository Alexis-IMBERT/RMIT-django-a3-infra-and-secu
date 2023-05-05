from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Alumni


def hello(request):
    alumnis = Alumni.objects.all()
    print(alumnis[0].username)
    return render(request, "listings/hello.html", {"alumnis": alumnis})


def home(request):
    return render(request, "listings/home.html")


def login(request):
    return render(request, "listings/login.html")


def register(request):
    return render(request, "listings/register.html")


def diploma_number(request):
    return render(request, "listings/diploma_number.html")
