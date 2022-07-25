import psycopg2
import logging
import os, sys
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)])

query = "INSERT INTO crop_yield_weather.weather (date, maximum_temperature, " \
        "minimum_temperature, amount_of_precipitation, weather_station) VALUES (%s, %s, %s, %s, %s)"

conn = None
try:
    # connect to the PostgreSQL server
    conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="Password@2023")
    cur = conn.cursor()
    records = []

    # Read all the files for weather data and load to database
    for filename in os.listdir("/Users/swetha/Development/weather-coding-exercise/code-challenge-template/wx_data"):
        with open(os.path.join("/Users/swetha/Development/weather-coding-exercise/code-challenge-template/wx_data", filename), 'r') as file:
            logging.info("Reading text file")
            file_content = file.readlines()
            values = [line.strip().split('\t') for line in file_content]
            filename = filename.replace('.txt', '')
            for val in values:
                val.append(filename)
                records.append(val)

    logging.info("Executing the query")
    logging.info("Start inserting records at: {}".format(datetime.now()))
    for rec in records:
        cur.execute(query, rec)
    logging.info("End inserting records at: {}".format(datetime.now()))
    logging.info("Total number of records inserted: {}".format(len(records)))
    cur.close()
    conn.commit()

except Exception as error:
    print(error)
