from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_show_courses),
    path('add_course', views.add_course),
    path('courses/destroy/<int:id>/', views.destroy_course),
    path('remove', views.remove_course)
]