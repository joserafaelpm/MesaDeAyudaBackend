# Generated by Django 4.2.1 on 2023-05-22 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_rename_rol_id_usuario_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(default=int, on_delete=django.db.models.deletion.CASCADE, to='usuarios.rol'),
            preserve_default=False,
        ),
    ]
