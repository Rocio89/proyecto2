# Generated by Django 2.0.2 on 2018-03-13 00:14

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=8, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField(default=datetime.date.today)),
                ('sexo', models.CharField(max_length=1)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono1', models.CharField(max_length=50)),
                ('telefono2', models.CharField(max_length=50)),
                ('fotocopia_ceudla', models.ImageField(upload_to='media_root', verbose_name='Imagen')),
            ],
        ),
    ]