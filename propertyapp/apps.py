from django.apps import AppConfig

class PropertyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'propertyapp'

    def ready(self):
        import propertyapp.signals  # Ensu