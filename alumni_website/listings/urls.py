from django.urls import path
from listings import views

urlpatterns =[
	path('',views.home, name='home'),
    path('home/', views.home),
     path('hello/', views.hello),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('diploma_number/', views.diploma_number, name='diploma_number'),
]