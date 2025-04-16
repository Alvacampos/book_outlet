from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('book/<slug:slug>', views.book_detail, name='book_detail'),
]
