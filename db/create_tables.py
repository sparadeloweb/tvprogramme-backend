import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

pg_host = os.getenv('POSTGRES_HOST')
pg_port = os.getenv('POSTGRES_PORT')
pg_database = os.getenv('POSTGRES_DB')
pg_user = os.getenv('POSTGRES_USER')
pg_password = os.getenv('POSTGRES_PASSWORD')

try:

    connection_parameters = f"host={pg_host} port={pg_port} dbname={pg_database} user={pg_user} password={pg_password}"
    connection = psycopg2.connect(connection_parameters)
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS channels (cid varchar NOT NULL PRIMARY KEY, logo_src text, name varchar NOT NULL);") # Crea tabla (si no existe) para los canales

    cursor.execute("CREATE TABLE IF NOT EXISTS programmes (pid integer PRIMARY KEY,\
                                                            cid varchar,\
                                                            main_title varchar,\
                                                            original_title varchar,\
                                                            subtitle varchar,\
                                                            country varchar,\
                                                            category varchar,\
                                                            subcategory varchar,\
                                                            description text,\
                                                            year_date varchar,\
                                                            image text,\
                                                            start_time varchar,\
                                                            finish_time varchar,\
                                                            CONSTRAINT fk_channels FOREIGN KEY(cid) REFERENCES channels(cid));")

    connection.commit() # Hago un commit a la base de datos

except (Exception, psycopg2.Error) as error:

    print(error)


