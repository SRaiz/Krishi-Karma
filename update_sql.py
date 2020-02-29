import csv
import os

import psycopg2

data_filename = 'crops.csv'
 
SQL = 'INSERT INTO crops_crop (name, image_url) VALUES (%s, %s)'


with open(data_filename, 'rt') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)    # Removed the 1st line which is header

    conn = psycopg2.connect(
        user = os.environ.get('DB_USER'),
        password = os.environ.get('DB_PASSWORD'),
        host = os.environ.get('DB_HOST'),
        port = '5432',
        database = os.environ.get('DB_NAME')
    )

    cursor = conn.cursor()
    cursor.executemany(SQL, reader)
