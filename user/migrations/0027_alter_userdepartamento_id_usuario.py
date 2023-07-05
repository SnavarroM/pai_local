# Generated by Django 4.1 on 2022-09-27 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0026_alter_userdepartamento_id_departamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdepartamento',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuario_dpto', to=settings.AUTH_USER_MODEL, verbose_name='usuario_dpto'),
        ),
    ]
