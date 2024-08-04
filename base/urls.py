from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list-pamong/', views.list_pamong, name='list-pamong'),
    path('tambah-pamong/', views.tambah_pamong, name='tambah-pamong'),
]