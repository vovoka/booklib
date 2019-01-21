from django.urls import path
from booklib import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booklib/', views.booklib_index, name='booklib_index'),
    path('stat/', views.booklib_statistics, name='stat'),

    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),



    # url(r'^books/$', views.BookListView.as_view(), name='books'),
    # url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]

