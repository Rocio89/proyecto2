# Generated by Django 2.0.2 on 2018-06-07 02:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0025_operacioncaja'),
    ]

    operations = [
        migrations.AddField(
            model_name='operacioncaja',
            name='concepto',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='operacioncaja',
            name='descripcion',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='operacioncaja',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='operacioncaja',
            name='monto',
            field=models.IntegerField(default=0),
        ),
    ]