# Generated by Django 2.0.2 on 2018-05-05 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='rol',
            field=models.CharField(default='staff', max_length=50, null=True),
        ),
    ]
