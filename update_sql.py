import csv
import os

import pandas as pd
import psycopg2


# This function upload csv to a target table
def pg_load_table(file_path, table_name, dbname, host, port, user, pwd):
    try:
        conn = psycopg2.connect(
            dbname = dbname, 
            host = host, 
            port = port,
            user = user, 
            password = pwd
        )
        print("Connecting to Database")
        cursor = conn.cursor()
        f = open(file_path, "r")
        
        # Truncate the table first
        cursor.execute("Truncate {} Cascade;".format(table_name))
        print("Truncated {}".format(table_name))
        
        # Load table from the file with header
        cursor.copy_expert(
            "copy {} from STDIN CSV HEADER QUOTE '\"'".format(table_name), f
        )
        
        cursor.execute("commit;")
        print("Loaded data into {}".format(table_name))
        conn.close()
        print("DB connection closed.")

    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)

pg_load_table(
    '/Users/sidharthraizada/Krishi-Karma/Final_Crop_Yield_Karnataka.csv',
    'public.crops_yield',
    os.environ.get('DB_NAME'),
    os.environ.get('DB_HOST'),
    os.environ.get('DB_PORT'),
    os.environ.get('DB_USER'),
    os.environ.get('DB_PASSWORD')
)
