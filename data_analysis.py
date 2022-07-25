import psycopg2
import logging
import itertools
from datetime import datetime
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)])

weather_query = "select * from crop_yield_weather.weather"

conn = None
try:
    # connect to the PostgreSQL server
    conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="Password@2023")
    cur = conn.cursor()
    cur.execute(weather_query)
    weather_records = cur.fetchall()
    statistics = {}

    # Group data based on year and station and calculate statistics
    for key, group in itertools.groupby(weather_records, lambda x: str(x[0].year) + "_" + x[4]):
        key_and_group = {key: list(group)}
        avg_max_temp = [(sum([val[1] for val in ele if val[1] != -9999])/len(ele))/10 for ele in key_and_group.values()]
        avg_min_temp = [(sum([val[2] for val in ele if val[2] != -9999])/len(ele))/10 for ele in key_and_group.values()]
        tot_accum_precip = [(sum([val[3] for val in ele if val[3] != -9999]))/100 for ele in key_and_group.values()]
        year_and_station = key.split("_")
        statistics[key] = [avg_max_temp[0], avg_min_temp[0], tot_accum_precip[0], int(year_and_station[0]), year_and_station[1]]

    statistics_query = "INSERT INTO crop_yield_weather.weather_statistics (avg_max_temp, avg_min_temp, " \
                       "total_accum_precipitation, " \
                       "year, weather_station) VALUES (%s, %s, %s, %s, %s)"

    logging.info("Executing the query")
    logging.info("Start inserting records at: {}".format(datetime.now()))
    for key, val in statistics.items():
        cur.execute(statistics_query, val)
    logging.info("End inserting records at: {}".format(datetime.now()))
    logging.info("Total number of records inserted: {}".format(len(statistics)))

    cur.close()
    conn.commit()

except Exception as error:
    print(error)
