from django.urls import path
from .views import (GenreCreateViews, GenreListViews,
                    AuthersListViews,AuthersCreateViews, AuthersUpdateViews,AuthersDeleteViews,
                    BookListViews,BookCreateViews,BookUpdateViews,BookDeleteViews)

urlpatterns = [
    # genre api
    path('genre/all/',GenreListViews.as_view(),name='genre_all'),
    path('genre/create/',GenreCreateViews.as_view(),name='genre_create'),
    # Auther api
    path('auther/all/',AuthersListViews.as_view(),name='auther_list'),
    path('auther/create/',AuthersCreateViews.as_view(), name='auther_create'),
    path('auther/update/<int:pk>',AuthersUpdateViews.as_view(),name='auther_update'),
    path('auther/delete/<int:pk>',AuthersDeleteViews.as_view(),name='auther_delete'),
    #  Book api
    path('book/all/',BookListViews.as_view(),name='book_list'),
    path('book/create/',BookCreateViews.as_view(), name='book_create'),
    path('book/update/<int:pk>',BookUpdateViews.as_view(),name='book_update'),
    path('book/delete/<int:pk>',BookDeleteViews.as_view(),name='book_delete'),
    
]