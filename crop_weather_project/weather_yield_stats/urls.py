from django.urls import include, path
from django.contrib import admin
from .views import CropYieldList, WeatherList, WeatherStatisticsList

app_name = "weather_yield_stats"
urlpatterns = [
    path('api/weather/', WeatherList.as_view(), name='weather'),
    path('api/yield/', CropYieldList.as_view(), name='yield'),
    path('api/weather/stats/', WeatherStatisticsList.as_view(), name='weather_stats'),
]
