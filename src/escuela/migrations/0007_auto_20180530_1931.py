# Generated by Django 2.0.2 on 2018-05-30 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0006_auto_20180527_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='escuela.Grupo'),
        ),
    ]