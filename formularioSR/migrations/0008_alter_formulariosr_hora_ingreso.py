# Generated by Django 4.1 on 2022-12-14 21:03

from django.db import migrations, models
import time


class Migration(migrations.Migration):

    dependencies = [
        ('formularioSR', '0007_alter_formulariosrderivacion_id_formulario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulariosr',
            name='hora_ingreso',
            field=models.TimeField(default=time.time, verbose_name='Hora Ingreso'),
        ),
    ]
