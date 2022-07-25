from rest_framework import serializers
from .models import Cropyield, Weather, WeatherStatistics


class CropyieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cropyield
        fields = "__all__"


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = "__all__"


class WeatherStatisticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherStatistics
        fields = "__all__"
