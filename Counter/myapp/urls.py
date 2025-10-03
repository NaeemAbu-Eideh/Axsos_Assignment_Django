from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path("destroy_session/", views.destroy),
    path("restart", views.destroy),
    path("increment-by-2", views.increment_by_two),
    path("increment-by-number", views.increment_by_number)
]