from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_signup_page),
    path('register', views.register),
    path('books/', views.all_books_page),
    path('signin', views.signin),
    path('books/logout', views.logout),
    path('books/add_favorite_book', views.add_favorite_bbok),
    path('flush/', views.flush),
    path('books/add_to_your_favoriets', views.add_to_your_favoriets),
    path('books/<int:id>/', views.show_book_details),
    path('books/<int:id>/delete_book', views.delete_book),
    path('/books/<int:id>/update_book_details', views.update_book_details),
    path('books/<int:id>/un_favorite', views.un_favorite),
    path('books/<int:id>/add_to_your_favoriets_in_info', views.add_to_your_favoriets_in_info),
    path('books/<int:id>/logout', views.logout)
]
