# Generated by Django 2.0.2 on 2018-05-27 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0020_ventacabecera_total_iva_exentas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.AddField(
            model_name='producto',
            name='control_stock',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='CategoriaProducto',
        ),
    ]
