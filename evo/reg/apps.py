from django.apps import AppConfig


class RegConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reg'

#import and use signal
    def ready(self):
        import reg.signals