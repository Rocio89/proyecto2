# Generated by Django 2.0.2 on 2018-05-13 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0010_auto_20180512_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compradetalle',
            name='producto',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
