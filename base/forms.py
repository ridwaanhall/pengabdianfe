from django import forms
from .models import Pamong, User

class PamongForm(forms.ModelForm):
    class Meta:
        model = Pamong
        fields = [
            'nama', 'nik', 'tempat_lahir', 'tanggal_lahir', 'alamat', 'status_kawin',
            'pekerjaan', 'gol_darah', 'jenis_kelamin', 'agama', 'nip', 'jabatan',
            'masa_jabatan_mulai', 'masa_jabatan_selesai', 'pendidikan_terakhir', 'foto'
        ]

class UserForm(forms.ModelForm):
    password_text = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['pamong', 'username', 'password_text', 'email', 'is_admin']
