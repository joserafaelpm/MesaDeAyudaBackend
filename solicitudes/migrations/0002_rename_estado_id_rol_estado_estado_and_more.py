# Generated by Django 4.2.1 on 2023-05-22 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rol_estado',
            old_name='estado_id',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='rol_estado',
            old_name='rol_id',
            new_name='rol',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='actividad_id',
            new_name='actividad',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='estado_id',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='usuario_id_solicitante',
            new_name='usuario_solicitante',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='usuario_id_tecnico',
            new_name='usuario_tecnico',
        ),
    ]