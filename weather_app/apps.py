from django.apps import AppConfig

class WeatherAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather_app'

    def ready(self):
        from .tasks import start_weather_updates
        start_weather_updates()