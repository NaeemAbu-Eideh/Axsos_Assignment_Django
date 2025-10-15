from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_signup_page),
    path('register', views.register),
    path('books/', views.all_books_page),
    path('signin', views.signin),
    path('logout', views.logout),
    path('add_favorite_book', views.add_favorite_bbok),
    path('flush/', views.flush),
    path('add_to_your_favoriets', views.add_to_your_favoriets),
    path('books/<int:id>/', views.show_book_details),
    path('delete_book', views.delete_book),
    path('update_book_details', views.update_book_details),
    path('un_favorite', views.un_favorite),
    path('add_to_your_favoriets_in_info', views.add_to_your_favoriets_in_info)
]
