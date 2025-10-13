from django.urls import path
from . import views

urlpatterns = [
    path('shows/new/', views.add_show),
    path('shows/<int:id>/edit/', views.edit_show),
    path('shows/', views.all_shows),
    path('shows/<int:id>/', views.tv_show),
    path('add_show', views.insert_show),
    path('edit_view', views.update_show)
]