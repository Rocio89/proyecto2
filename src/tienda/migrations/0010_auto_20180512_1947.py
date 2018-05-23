# Generated by Django 2.0.2 on 2018-05-12 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0009_auto_20180510_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='compracabecera',
            name='nro_factura',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='compracabecera',
            name='total_iva',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='compracabecera',
            name='total_iva_10',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='compracabecera',
            name='total_iva_5',
            field=models.IntegerField(default=0),
        ),
    ]