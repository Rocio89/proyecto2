# Generated by Django 2.0.2 on 2018-05-31 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0009_auto_20180530_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='estado',
            field=models.CharField(choices=[('A', 'ACTIVO'), ('IN', 'INACTIVO')], default='A', max_length=2),
        ),
    ]