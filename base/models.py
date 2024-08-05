from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class Pamong(models.Model):
    nama = models.CharField(max_length=100)
    nik = models.CharField(max_length=16, unique=True)
    nip = models.CharField(max_length=18, unique=True, blank=True, null=True)
    tempat_lahir = models.CharField(max_length=50, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    status_kawin = models.CharField(max_length=20, choices=[
        ("Belum Kawin", "Belum Kawin"),
        ("Kawin", "Kawin"),
        ("Cerai Hidup", "Cerai Hidup"),
        ("Cerai Mati", "Cerai Mati")
    ], blank=True, null=True)
    pekerjaan = models.CharField(max_length=50, blank=True, null=True)
    jabatan = models.CharField(max_length=50, blank=True, null=True)
    gol_darah = models.CharField(max_length=2, choices=[
        ("A", "A"),
        ("B", "B"),
        ("AB", "AB"),
        ("O", "O")
    ], blank=True, null=True)
    agama = models.CharField(max_length=20, blank=True, null=True)
    jenis_kelamin = models.CharField(max_length=1, choices=[
        ("L", "L"),
        ("P", "P")
    ], blank=True, null=True)
    masa_jabatan_mulai = models.IntegerField(blank=True, null=True)
    masa_jabatan_selesai = models.IntegerField(blank=True, null=True)
    pendidikan_terakhir = models.CharField(max_length=50, blank=True, null=True)
    foto = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.nama

class UserManager(BaseUserManager):
    def create_user(self, pamong_id, username, password, password_text, email=None, **extra_fields):
        try:
            pamong = Pamong.objects.get(id=pamong_id)
        except Pamong.DoesNotExist:
            raise ValueError(_('Pamong with the provided ID does not exist'))
        
        if not username:
            raise ValueError(_('The Username field must be set'))
        
        user = self.model(pamong=pamong, username=username, password_text=password_text, email=email, **extra_fields)
        user.set_password(password)  # This hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, pamong_id, username, password, password_text, email=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self.create_user(pamong_id, username, password, password_text, email, **extra_fields)
    

class User(AbstractBaseUser):
    pamong = models.OneToOneField(Pamong, on_delete=models.CASCADE, related_name='user')
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # This will store the hashed password
    password_text = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(unique=True, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['pamong_id']

    def __str__(self):
        return self.username