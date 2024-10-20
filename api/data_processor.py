from django.utils import timezone
from django.db.models import Avg, Max, Min
from collections import Counter
from weather_app.models import WeatherData, DailySummary, Alert
from api.weather_api import get_weather_data
from django.conf import settings

def process_weather_data():
    for city in settings.MONITORED_CITIES:
        data = get_weather_data(city)
        if data:
            WeatherData.objects.create(
                city=data['city'],
                main=data['main'],
                temp=data['temp'],
                feels_like=data['feels_like'],
                timestamp=timezone.datetime.fromtimestamp(data['timestamp'], tz=timezone.utc)
            )
            check_alert(data)

def create_daily_summary():
    today = timezone.now().date()
    for city in settings.MONITORED_CITIES:
        daily_data = WeatherData.objects.filter(city=city, timestamp__date=today)
        if daily_data.exists():
            avg_temp = daily_data.aggregate(Avg('temp'))['temp__avg']
            max_temp = daily_data.aggregate(Max('temp'))['temp__max']
            min_temp = daily_data.aggregate(Min('temp'))['temp__min']
            conditions = daily_data.values_list('main', flat=True)
            dominant_condition = Counter(conditions).most_common(1)[0][0]

            DailySummary.objects.update_or_create(
                city=city,
                date=today,
                defaults={
                    'avg_temp': avg_temp,
                    'max_temp': max_temp,
                    'min_temp': min_temp,
                    'dominant_condition': dominant_condition
                }
            )

def check_alert(data):
    if data['temp'] > settings.TEMPERATURE_ALERT_THRESHOLD:
        Alert.objects.create(
            city=data['city'],
            message=f"Temperature alert: {data['temp']}°C exceeds threshold of {settings.TEMPERATURE_ALERT_THRESHOLD}°C"
        )