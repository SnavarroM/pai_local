# Generated by Django 4.1 on 2022-12-06 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularioInsumos', '0004_alter_formularioinsumo_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='formularioinsumo',
            name='cantidad_aprobada_jefatura',
            field=models.IntegerField(default=0, verbose_name='Cantidad Aprobada por Jefatura'),
        ),
        migrations.AddField(
            model_name='formularioinsumo',
            name='cantidad_entregada',
            field=models.IntegerField(default=0, verbose_name='Cantidad Entregada'),
        ),
    ]
