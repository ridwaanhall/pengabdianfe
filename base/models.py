from django.db import models

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
