
import sys
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

pg_host = os.getenv('POSTGRES_HOST')
pg_port = os.getenv('POSTGRES_PORT')
pg_database = os.getenv('POSTGRES_DB')
pg_user = os.getenv('POSTGRES_USER')
pg_password = os.getenv('POSTGRES_PASSWORD')

from db.channels_id_array_list import home as home_id_channels

def get_home_programmes () :

    try:

        connection_parameters = f"host={pg_host} port={pg_port} dbname={pg_database} user={pg_user} password={pg_password}"
        connection = psycopg2.connect(connection_parameters)
        cursor = connection.cursor()

        sql = 'SELECT * from programmes WHERE cid = ANY (%s)'
        cursor.execute(sql, (home_id_channels,))

        programmes = cursor.fetchall()

        return programmes

    except (Exception, psycopg2.Error) as error:

        print(error)
