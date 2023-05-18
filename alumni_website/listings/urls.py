from django.urls import path#, include
from listings import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home),
    path('hello/', views.hello),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms'),
    path('service/', views.service, name='service'),
    path('add-diploma/',views.add_diploma,name="add_diploma"),
    path('info-diploma/',views.info_diploma,name="info_diploma"),
    path('check-diploma/',views.check_diploma,name="check_diploma"),
    path('contact-us/',views.contact,name="contact"),

]
