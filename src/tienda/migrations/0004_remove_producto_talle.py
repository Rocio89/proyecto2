# Generated by Django 2.0.2 on 2018-04-25 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_producto_talle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='talle',
        ),
    ]
