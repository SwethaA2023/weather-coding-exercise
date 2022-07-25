
------------------Problem 1 -----------------------------------------
CREATE DATABASE IF NOT EXISTS postgres;

CREATE SCHEMA IF NOT EXISTS crop_yield_weather AUTHORIZATION postgres;

CREATE TABLE IF NOT EXISTS crop_yield_weather.weather(
    date DATE,
    maximum_temperature INT,
    minimum_temperature INT,
    amount_of_precipitation INT,
    weather_station VARCHAR(11),
    CONSTRAINT date_station_constraint UNIQUE (date, weather_station)
);


CREATE TABLE IF NOT EXISTS crop_yield_weather.cropyield(
  year INT,
  total_amount INT,
  CONSTRAINT date_constraint UNIQUE (year)
);


------------------Problem 3 -----------------------------------------

CREATE TABLE IF NOT EXISTS crop_yield_weather.weather_statistics(
    avg_max_temp float null,
    avg_min_temp float null,
    total_accum_precipitation INT,
    year INT,
    weather_station VARCHAR(11),
    CONSTRAINT year_station_constraint UNIQUE (year, weather_station)
);



