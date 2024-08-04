from django.shortcuts import render

# content
def index(request):
    return render(request, 'index.html')


# pamong
def list_pamong(request):
    return render(request, 'list-pamong.html')

def edit_pamong(request):
    return render(request, 'edit-pamong.html')

def tambah_pamong(request):
    return render(request, 'tambah-pamong.html')


# kegiatan
def list_kegiatan(request):
    return render(request, 'list-kegiatan.html')

def edit_kegiatan(request):
    return render(request, 'edit-kegiatan.html')

def tambah_kegiatan(request):
    return render(request, 'tambah-kegiatan.html')


# auth
def login(request):
    return render(request, 'login.html')

def forgot_password(request):
    return render(request, 'forgot-password.html')
