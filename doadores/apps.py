from django.apps import AppConfig


class DoadoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'doadores'

    
    
    def ready(self):
        import doadores.signals

