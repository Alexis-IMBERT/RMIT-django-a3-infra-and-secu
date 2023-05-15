from django.urls import path#, include
from listings import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home),
    path('hello/', views.hello),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    # path('diploma_number/', views.diploma_number, name='diploma_number'),
    path('terms_and_conditions', views.terms_and_conditions, name='terms'),
    path('service', views.service, name='service'),

]
