import threading
import time
from django.conf import settings
from api.data_processor import process_weather_data, create_daily_summary

def run_weather_updates():
    while True:
        process_weather_data()
        create_daily_summary()
        time.sleep(settings.WEATHER_UPDATE_INTERVAL)

def start_weather_updates():
    thread = threading.Thread(target=run_weather_updates)
    thread.daemon = True
    thread.start()