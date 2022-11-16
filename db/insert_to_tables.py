import sys
import os
from dotenv import load_dotenv
import psycopg2
from get_programmes import parseXML

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

    cursor.execute("TRUNCATE channels CASCADE;")
    cursor.execute("TRUNCATE programmes CASCADE;")

    connection.commit()

    channels = parseXML('outputs/all.xml')

    counter = 0

    for channel in channels :

        channel_name = channel['name'].replace("'", "%REPLACEFORCOLON%")
        channel_id = channel['id']
        channel_logo_src = channel['logo_src'] if channel.__contains__('logo_src') else None

        cursor.execute(f"INSERT INTO channels \
                            (cid, logo_src, name) \
                            VALUES ('{channel_id}', '{channel_logo_src}', '{channel_name}');")

        connection.commit()
        
        channel_programmes = channel['programmes']

        for programme in channel_programmes :

            programme_name = programme['main_title'].replace("'", "%REPLACEFORCOLON%")
            programme_cid = programme['channel_id']
            programme_original_title = programme['original_title'].replace("'", " ") if programme.__contains__('original_title') else None
            programme_subtitle = programme['subtitle'].replace("'", " ") if programme.__contains__('subtitle') else None
            programme_country = programme['country'].replace("'", " ") if programme.__contains__('country') else None
            programme_category = programme['category'].replace("'", " ") if programme.__contains__('category') else None
            programme_subcategory = programme['subcategory'].replace("'", " ") if programme.__contains__('subcategory') else None
            programme_description = programme['description'].replace("'", " ") if programme.__contains__('description') else None
            programme_year_date = programme['year_date'].replace("'", " ") if programme.__contains__('year_date') else None
            programme_image = programme['image'].replace("'", " ") if programme.__contains__('image') else None
            programme_start_time = programme['start_time'].replace("'", " ") if programme.__contains__('start_time') else None
            programme_finish_time = programme['finish_time'].replace("'", " ") if programme.__contains__('finish_time') else None

            cursor.execute(f"INSERT INTO programmes \
                            (pid, cid, main_title, original_title, subtitle, country, category, subcategory, description, year_date, image, start_time, finish_time) \
                            VALUES ('{counter}', '{programme_cid}', '{programme_name}', '{programme_original_title}', '{programme_subtitle}', '{programme_country}', '{programme_category}', \
                                    '{programme_subcategory}', '{programme_description}', '{programme_year_date}', '{programme_image}', '{programme_start_time}', '{programme_finish_time}');")

            connection.commit()

            counter += 1
    

except (Exception, psycopg2.Error) as error:

    print(error)
