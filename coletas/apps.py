from django.apps import AppConfig


class ColetaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coletas'


    def ready(self):
            import coletas.signals

