from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
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
    def create_user(self, pamong_id, username, password=None, password_text=None, email=None, **extra_fields):
        try:
            pamong = Pamong.objects.get(id=pamong_id)
        except Pamong.DoesNotExist:
            raise ValueError(_('Pamong with the provided ID does not exist'))

        if not username:
            raise ValueError(_('The Username field must be set'))

        if not password:
            raise ValueError(_('The Password field must be set'))

        user = self.model(pamong=pamong, username=username, password_text=password_text, email=email, **extra_fields)
        user.set_password(password)  # This hashes the password
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, pamong_id, username, password=None, password_text=None, email=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        return self.create_user(pamong_id, username, password, password_text, email, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    pamong = models.OneToOneField(Pamong, on_delete=models.CASCADE, related_name='user')
    username = models.CharField(max_length=150, unique=True)
    password_text = models.CharField(max_length=128, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Ensure this field is present
    email = models.EmailField(unique=True, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['pamong_id']

    def __str__(self):
        return self.username

    # Ensure this is removed as it conflicts with the BooleanField
    # @property
    # def is_staff(self):
    #     return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # Adding related_name to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='base_user_set',
        blank=True,
        help_text=_('Groups this user belongs to. A user will get all permissions granted to the groups they belong to.'),
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='base_user_set',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_query_name='user'
    )