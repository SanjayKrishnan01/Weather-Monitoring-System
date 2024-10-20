from django.shortcuts import render
from django.utils import timezone
from .models import WeatherData, DailySummary, Alert
from api.data_processor import process_weather_data, create_daily_summary
from django.db.models import Max

def index(request):
    process_weather_data()
    create_daily_summary()

    latest_timestamps = WeatherData.objects.values('city').annotate(latest_timestamp=Max('timestamp'))
    latest_weather = []
    for item in latest_timestamps:
        latest_weather.append(WeatherData.objects.filter(
            city=item['city'], 
            timestamp=item['latest_timestamp']
        ).first())

    daily_summaries = DailySummary.objects.filter(date=timezone.now().date())
    alerts = Alert.objects.order_by('-timestamp')[:5]
    
    context = {
        'latest_weather': latest_weather,
        'daily_summaries': daily_summaries,
        'alerts': alerts,
    }
    return render(request, 'weather_app/index.html', context)

def daily_summary(request):
    summaries = DailySummary.objects.order_by('-date')
    return render(request, 'weather_app/daily_summary.html', {'summaries': summaries})