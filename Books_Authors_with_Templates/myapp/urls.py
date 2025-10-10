from django.urls import path
from . import views

urlpatterns = [
    path('', views.go_to_books),
    path('authors/', views.go_to_auther),
    path("books/<int:id>", views.show_book),
    path('<int:id>/', views.show_author),
    path('flush/', views.flush),
    path('add-book', views.add_book),
    path('add-author', views.add_author),
    path('add_book_to_author', views.add_book_to_author),
    path('add_author_to_book', views.add_auther_to_book),
]