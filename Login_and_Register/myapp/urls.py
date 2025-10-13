from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_signup),
    path('success/', views.success),
    path('register', views.register),
    path('login', views.login),
    path('flush/', views.flush),
    path('logout', views.logout)
]