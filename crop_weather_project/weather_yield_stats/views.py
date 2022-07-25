from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from .models import Cropyield, Weather, WeatherStatistics
from rest_framework import generics
from .serializers import CropyieldSerializer, WeatherSerializer, WeatherStatisticsSerializer


class CropYieldList(generics.ListAPIView):
    queryset = Cropyield.objects.all()
    serializer_class = CropyieldSerializer


class WeatherList(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer


class WeatherStatisticsList(generics.ListAPIView):
    queryset = WeatherStatistics.objects.all()
    serializer_class = WeatherStatisticsSerializer




