from django.urls import path
from booklib import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booklib/', views.booklib_index, name='booklib_index'),
    path('stat/', views.booklib_statistics, name='booklib_statistics'),
]
