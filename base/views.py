from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages


# auth
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username atau password salah, atau Anda bukan admin.')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('admin-login')

def forgot_password(request):
    return render(request, 'forgot-password.html')


# content
@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/login/')
def index(request):
    return render(request, 'index.html')


# pamong
@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/login/')
def list_pamong(request):
    return render(request, 'list-pamong.html')

@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/login/')
def edit_pamong(request):
    return render(request, 'edit-pamong.html')

@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/login/')
def tambah_pamong(request):
    return render(request, 'tambah-pamong.html')


# kegiatan
@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/login/')
def list_kegiatan(request):
    return render(request, 'list-kegiatan.html')

@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/login/')
def edit_kegiatan(request):
    return render(request, 'edit-kegiatan.html')

@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/login/')
def tambah_kegiatan(request):
    return render(request, 'tambah-kegiatan.html')

