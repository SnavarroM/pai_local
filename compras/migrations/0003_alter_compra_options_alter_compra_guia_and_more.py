# Generated by Django 4.1 on 2022-11-28 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_alter_compra_fecha_ingreso_compra'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compra',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='compra',
            name='guia',
            field=models.CharField(max_length=50, unique=True, verbose_name='Guía'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='orden_de_compra',
            field=models.CharField(max_length=50, unique=True, verbose_name='Orden de Compra'),
        ),
    ]
