from django.apps import AppConfig


class KamausConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kamaus'
    
    def ready(self):
        import kamaus.signals
    
#     from django.apps import AppConfig

# class MyappConfig(AppConfig):
#     name = 'myapp'

#     def ready(self):
#         import myapp.signals  # Ensure the signals are imported

