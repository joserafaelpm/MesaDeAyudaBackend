from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'

class CoreConfig(AppConfig):
    name = 'usuarios'
    label = 'usuarios'
