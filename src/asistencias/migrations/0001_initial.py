# Generated by Django 2.0.2 on 2018-03-12 21:04

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('alumnos', '0003_alumno_fecha_nacimiento'),
        ('grupos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('id_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.Alumno')),
                ('id_grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Grupo')),
            ],
        ),
    ]