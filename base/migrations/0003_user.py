# Generated by Django 4.2 on 2024-08-05 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_gambar_pamong_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password_text', models.CharField(max_length=128)),
                ('password_encrypted', models.CharField(blank=True, max_length=128, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('pamong', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.pamong')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
