from django.urls import path
from . import views

urlpatterns = [
    # content
    path('', views.index, name='index'),
    path('list-pamong/', views.list_pamong, name='list-pamong'),
    path('tambah-pamong/', views.tambah_pamong, name='tambah-pamong'),
    path('edit-pamong/', views.edit_pamong, name='edit-pamong'),
    
    # auth
    path('login/', views.login, name='login'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
]