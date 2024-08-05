from django import forms
from .models import Pamong

class PamongForm(forms.ModelForm):
    class Meta:
        model = Pamong
        fields = [
            'nama', 'nik', 'tempat_lahir', 'tanggal_lahir', 'alamat', 'status_kawin',
            'pekerjaan', 'gol_darah', 'jenis_kelamin', 'agama', 'nip', 'jabatan',
            'masa_jabatan_mulai', 'masa_jabatan_selesai', 'pendidikan_terakhir', 'foto'
        ]
