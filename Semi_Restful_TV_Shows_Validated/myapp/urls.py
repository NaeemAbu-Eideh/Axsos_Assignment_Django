from django.urls import path
from . import views

urlpatterns = [
    
    path('shows/', views.all_tv_shows),
    path('shows/<int:id>/', views.show_tv),
    path('shows/new/', views.add_new_show),
    path('shows/<int:id>/edit/', views.edit_show_page),
    path('delete', views.delete_show),
    path('add_show', views.add_show),
    path('edit_view', views.update_show)
]  