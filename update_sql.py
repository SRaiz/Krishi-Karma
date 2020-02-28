import csv

import psycopg2

data_filename = 'crops.csv'
 
SQL = 'INSERT INTO crops_crop (name, image_url) VALUES (%s, %s)'


with open(data_filename, 'rt') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)    # Removed the 1st line which is header

    with psycopg2.connect( user='postgres', password='tweety_336600', host="localhost", port="5432", database="krishi-karma" ) as conn:
        cursor = conn.cursor()
        cursor.executemany(SQL, reader)
