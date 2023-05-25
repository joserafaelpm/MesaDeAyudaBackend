from django.apps import AppConfig


class ActividadesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'actividades'

class CoreConfig(AppConfig):
    name = 'actividades'
    label = 'actividades'