from django.urls import path
from . import views

urlpatterns = [
    # content
    path('', views.index, name='index'),
    
    # pamong
    path('list-pamong/', views.list_pamong, name='list-pamong'),
    path('edit-pamong/', views.edit_pamong, name='edit-pamong'),
    path('tambah-pamong/', views.tambah_pamong, name='tambah-pamong'),
    
    # kegiatan
    path('list-kegiatan/', views.list_kegiatan, name='list-kegiatan'),
    path('edit-kegiatan/', views.edit_kegiatan, name='edit-kegiatan'),
    path('tambah-kegiatan/', views.tambah_kegiatan, name='tambah-kegiatan'),
    
    # auth
    path('login/', views.login, name='login'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
]