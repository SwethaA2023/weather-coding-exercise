import psycopg2
import logging
from datetime import datetime
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)])


query = "INSERT INTO crop_yield_weather.cropyield (YEAR, TOTAL_AMOUNT) VALUES (%s, %s)"

conn = None
try:
    # connect to the PostgreSQL server
    conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="Password@2023")
    cur = conn.cursor()

    # Read data from file and Insert data to the database
    with open("/Users/swetha/Development/weather-coding-exercise/code-challenge-template/yld_data/US_corn_grain_yield.txt", 'r') as file:
        logging.info("Reading text file")
        file_content = file.readlines()
        values = [line.strip().split('\t') for line in file_content]

        logging.info("Executing the query")
        logging.info("Start inserting records at: {}".format(datetime.now()))
        for rec in values:
            cur.execute(query, rec)
        logging.info("End inserting records at: {}".format(datetime.now()))
        logging.info("Total number of records inserted: {}".format(len(values)))

    cur.close()
    conn.commit()
except Exception as error:
    print(error)
