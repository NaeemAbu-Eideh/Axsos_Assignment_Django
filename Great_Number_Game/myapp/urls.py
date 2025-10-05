from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('input', views.input),
    path('newPage/', views.newPage),
    path("replay", views.play_again),
    path("flush",views.fulsh)
]