from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_signup),
    path('register', views.register),
    path('signin', views.login),
    path('flush/', views.flush),
]