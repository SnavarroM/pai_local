# Generated by Django 4.1 on 2022-11-24 13:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuraciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuraciones',
            name='ultima_actualizacion',
            field=models.DateField(default=datetime.datetime(2022, 11, 24, 10, 40, 27, 614796), verbose_name='Última Actualización'),
        ),
    ]
