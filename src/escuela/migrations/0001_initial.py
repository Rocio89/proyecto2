# Generated by Django 2.0.2 on 2018-03-25 00:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('id_alumno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=150)),
                ('costo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DiaHora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('L', 'Lunes'), ('M', 'Martes'), ('X', 'Miercoles'), ('J', 'Jueves'), ('V', 'Viernes')], max_length=1)),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='EtiquetaClase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etiqueta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escuela.Etiqueta')),
                ('id_clase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escuela.Clase')),
            ],
        ),
        migrations.CreateModel(
            name='EtiquetaGrupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etiqueta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escuela.Etiqueta')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cupo_maximo', models.IntegerField(default=0)),
                ('costo', models.IntegerField(default=0)),
                ('id_clase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escuela.Clase')),
                ('id_profesor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(default=datetime.date.today)),
                ('fecha_fin', models.DateField(default=datetime.date.today)),
                ('id_alumno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Alumno')),
                ('id_grupo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escuela.Grupo')),
            ],
        ),
        migrations.AddField(
            model_name='etiquetagrupo',
            name='id_grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escuela.Grupo'),
        ),
        migrations.AddField(
            model_name='diahora',
            name='id_grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escuela.Grupo'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='id_grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escuela.Grupo'),
        ),
    ]
