# Generated by Django 4.2 on 2024-08-05 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pamong',
            old_name='gambar',
            new_name='foto',
        ),
    ]