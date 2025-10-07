from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('flush/', views.flush),
    path('add_dojo', views.add_dojo), 
    path('add_ninja', views.add_ninja)
]