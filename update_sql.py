# import csv

# import psycopg2

# data_filename = 'crops.csv'
 
# SQL = """
# INSERT INTO crops_crop (name, image_url)
# VALUES (:name, :image_url)
# """

# with open(data_filename, 'rt') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     with psycopg2.connect( "dbname='Krishi-Karma' user='postgres' password='tweety_336600'" ) as conn:
#         cursor = conn.cursor()
#         cursor.executemany(SQL, csv_reader)
