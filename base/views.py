from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from .models import Pamong, User

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
        try:
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

            if 'foto' in request.FILES:
                pamong.foto = request.FILES['foto']

            # Cek apakah NIP atau NIK sudah ada, tapi bukan untuk pamong yang sedang diedit
            if Pamong.objects.filter(nip=nip).exclude(id=pk).exists():
                messages.error(request, 'NIP sudah terdaftar. Silakan gunakan NIP yang lain.')
            elif Pamong.objects.filter(nik=nik).exclude(id=pk).exists():
                messages.error(request, 'NIK sudah terdaftar. Silakan gunakan NIK yang lain.')
            else:
                # Update data pamong
                pamong.nama = nama
                pamong.nik = nik
                pamong.tempat_lahir = tempat_lahir
                pamong.tanggal_lahir = tanggal_lahir
                pamong.alamat = alamat
                pamong.status_kawin = status_kawin
                pamong.pekerjaan = pekerjaan
                pamong.gol_darah = gol_darah
                pamong.jenis_kelamin = jenis_kelamin
                pamong.agama = agama
                pamong.nip = nip
                pamong.jabatan = jabatan
                pamong.masa_jabatan_mulai = masa_jabatan_mulai
                pamong.masa_jabatan_selesai = masa_jabatan_selesai
                pamong.pendidikan_terakhir = pendidikan_terakhir
                
                pamong.save()
                messages.success(request, 'Data pamong berhasil diperbarui.')
                return redirect('detail-edit-pamong', pk=pamong.id)
        except IntegrityError as e:
            messages.error(request, f'Terjadi kesalahan: {str(e)}')

    context = {
        'pamong': pamong
    }
    return render(request, 'detail-edit-pamong.html', context)

@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/login/')
def tambah_pamong(request):
    if request.method == 'POST':
        try:
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

            # Cek apakah NIP sudah ada
            if Pamong.objects.filter(nip=nip).exists():
                messages.error(request, 'NIP sudah terdaftar. Silakan gunakan NIP yang lain.')
            elif Pamong.objects.filter(nik=nik).exists():
                messages.error(request, 'NIK sudah terdaftar. Silakan gunakan NIK yang lain.')
            else:
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
                messages.success(request, 'Data pamong berhasil ditambahkan.')
                return redirect('list-pamong')
        except IntegrityError as e:
            messages.error(request, f'Terjadi kesalahan: {str(e)}')
    
    return render(request, 'tambah-pamong.html')

@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/login/')
def hapus_pamong(request, pk):
    try:
        pamong = get_object_or_404(Pamong, id=pk)
        pamong.delete()
        messages.success(request, 'Data pamong berhasil dihapus.')
    except IntegrityError as e:
        messages.error(request, f'Terjadi kesalahan: {str(e)}')
    except Exception as e:
        messages.error(request, f'Terjadi kesalahan yang tidak terduga: {str(e)}')
    
    return redirect('list-pamong')


# user
@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/login/')
def list_user(request):
    user = User.objects.all()
    context = {
        'users': user
    }
    return render(request, 'list-user.html', context)

@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/login/')
def tambah_user(request):
    if request.method == 'POST':
        pamong_id = request.POST.get('pamong_id')
        username = request.POST.get('username')
        password = request.POST.get('password_text')
        password_text = request.POST.get('password_text')  # Changed to match form field name
        email = request.POST.get('email')
        is_admin = request.POST.get('is_admin') == 'on'
        is_staff = request.POST.get('is_staff') == 'on'
        is_active = request.POST.get('is_active') == 'on'

        try:
            pamong = Pamong.objects.get(id=pamong_id)
        except Pamong.DoesNotExist:
            messages.error(request, 'Pamong dengan ID tersebut tidak ditemukan.')
            return render(request, 'tambah-user.html')

        if User.objects.filter(pamong=pamong).exists():
            messages.error(request, 'User dengan Pamong ID tersebut sudah ada.')
            return render(request, 'tambah-user.html')

        try:
            user = User.objects.create_user(
                pamong_id=pamong.id,
                username=username,
                password=password,
                password_text=password_text,
                email=email,
            )
            user.is_staff = is_staff
            user.is_superuser = is_admin
            user.is_active = is_active
            user.save()
            messages.success(request, 'User berhasil ditambahkan.')
            return redirect('list-user')
        except IntegrityError as e:
            if 'UNIQUE constraint failed: base_user.email' in str(e):
                messages.error(request, 'Email sudah digunakan. Silakan gunakan email yang lain.')
            else:
                messages.error(request, f'Terjadi kesalahan: {str(e)}')
        except ValidationError as e:
            messages.error(request, f'Validasi error: {str(e)}')
        except Exception as e:
            messages.error(request, f'Terjadi kesalahan yang tidak terduga: {str(e)}')

    return render(request, 'tambah-user.html')

@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_admin, login_url='/login/')
def detail_edit_user(request, pk):
    user = get_object_or_404(User, id=pk)
    
    context = {
        'user': user
    }
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password_text')
        email = request.POST.get('email')
        is_admin = request.POST.get('is_admin') == 'on'
        is_staff = request.POST.get('is_staff') == 'on'
        is_active = request.POST.get('is_active') == 'on'

        # Validasi username
        if User.objects.filter(username=username).exclude(id=pk).exists():
            messages.error(request, 'Username sudah digunakan.')
            return render(request, 'detail-edit-user.html', context)

        # Validasi email
        if User.objects.filter(email=email).exclude(id=pk).exists():
            messages.error(request, 'Email sudah digunakan.')
            return render(request, 'detail-edit-user.html', context)

        try:
            # Update user
            user.username = username
            user.email = email
            if password:
                user.set_password(password)
                user.password_text = password  # Simpan password teks jika diperlukan
            user.is_staff = is_staff
            user.is_superuser = is_admin
            user.is_active = is_active
            user.save()

            messages.success(request, 'User berhasil diperbarui.')
            return redirect('detail-edit-user', pk=user.id)
        except IntegrityError as e:
            messages.error(request, f'Terjadi kesalahan saat menyimpan pengguna: {str(e)}')
        except ValidationError as e:
            messages.error(request, f'Validasi error: {str(e)}')
        except Exception as e:
            messages.error(request, f'Terjadi kesalahan yang tidak terduga: {str(e)}')

    return render(request, 'detail-edit-user.html', context)

@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/login/')
def hapus_user(request, pk):
    user = get_object_or_404(User, id=pk)
    user.delete()
    return redirect('list-user')


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

