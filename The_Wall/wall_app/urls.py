from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('logout', views.logout),
    path('add_message', views.post_message),
    path('wall/', views.go_to_comment_page),
    path('add_comment', views.post_comment)
]
