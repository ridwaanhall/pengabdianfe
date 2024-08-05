from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages

from .models import Pamong

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
    pamong = Pamong.objects.all()
    context = {
        'pamong': pamong
    }
    return render(request, 'list-pamong.html', context)

@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/login/')
def edit_pamong(request):
    return render(request, 'edit-pamong.html')

@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/login/')
def detail_edit_pamong(request, pk):
    pamong = Pamong.objects.get(id=pk)
    if request.method == 'POST':
        # Ambil data dari request.POST
        pamong.nama = request.POST.get('nama')
        pamong.nik = request.POST.get('nik')
        pamong.tempat_lahir = request.POST.get('tempat_lahir')
        pamong.tanggal_lahir = request.POST.get('tanggal_lahir')
        pamong.alamat = request.POST.get('alamat')
        pamong.status_kawin = request.POST.get('status_kawin')
        pamong.pekerjaan = request.POST.get('pekerjaan')
        pamong.gol_darah = request.POST.get('gol_darah')
        pamong.jenis_kelamin = request.POST.get('jenis_kelamin')
        pamong.agama = request.POST.get('agama')
        pamong.nip = request.POST.get('nip')
        pamong.jabatan = request.POST.get('jabatan')
        pamong.masa_jabatan_mulai = request.POST.get('masa_jabatan_mulai')
        pamong.masa_jabatan_selesai = request.POST.get('masa_jabatan_selesai')
        pamong.pendidikan_terakhir = request.POST.get('pendidikan_terakhir')
        
        if 'foto' in request.FILES:
            pamong.foto = request.FILES['foto']
            
        pamong.save()
        return redirect('list-pamong')
    
    context = {
        'pamong': pamong
    }

    return render(request, 'detail-edit-pamong.html', context)

@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/login/')
def tambah_pamong(request):
    if request.method == 'POST':
        # Ambil data dari request.POST
        nama = request.POST.get('nama')
        nik = request.POST.get('nik')
        tempat_lahir = request.POST.get('tempat_lahir')
        tanggal_lahir = request.POST.get('tanggal_lahir')
        alamat = request.POST.get('alamat')
        status_kawin = request.POST.get('status_kawin')
        pekerjaan = request.POST.get('pekerjaan')
        gol_darah = request.POST.get('gol_darah')
        jenis_kelamin = request.POST.get('jenis_kelamin')
        agama = request.POST.get('agama')
        nip = request.POST.get('nip')
        jabatan = request.POST.get('jabatan')
        masa_jabatan_mulai = request.POST.get('masa_jabatan_mulai')
        masa_jabatan_selesai = request.POST.get('masa_jabatan_selesai')
        pendidikan_terakhir = request.POST.get('pendidikan_terakhir')
        
        # Ambil file dari request.FILES
        foto = request.FILES.get('foto')

        # Simpan data ke database
        pamong = Pamong(
            nama=nama,
            nik=nik,
            tempat_lahir=tempat_lahir,
            tanggal_lahir=tanggal_lahir,
            alamat=alamat,
            status_kawin=status_kawin,
            pekerjaan=pekerjaan,
            gol_darah=gol_darah,
            jenis_kelamin=jenis_kelamin,
            agama=agama,
            nip=nip,
            jabatan=jabatan,
            masa_jabatan_mulai=masa_jabatan_mulai,
            masa_jabatan_selesai=masa_jabatan_selesai,
            pendidikan_terakhir=pendidikan_terakhir,
            foto=foto
        )
        pamong.save()
        return redirect('list-pamong')
    return render(request, 'tambah-pamong.html')

@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/login/')
def hapus_pamong(request, pk):
    pamong = get_object_or_404(Pamong, id=pk)
    pamong.delete()
    return redirect('list-pamong')


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

