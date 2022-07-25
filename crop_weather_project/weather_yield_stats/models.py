from django.db import models


class Cropyield(models.Model):
    year = models.IntegerField(unique=True, blank=True, primary_key=True)
    total_amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cropyield'


class Weather(models.Model):
    date = models.DateField(blank=True, primary_key=True)
    maximum_temperature = models.IntegerField(blank=True, null=True)
    minimum_temperature = models.IntegerField(blank=True, null=True)
    amount_of_precipitation = models.IntegerField(blank=True, null=True)
    weather_station = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather'
        unique_together = (('date', 'weather_station'),)


class WeatherStatistics(models.Model):
    avg_max_temp = models.FloatField(blank=True, null=True)
    avg_min_temp = models.FloatField(blank=True, null=True)
    total_accum_precipitation = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, primary_key=True)
    weather_station = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather_statistics'
        unique_together = (('year', 'weather_station'),)
