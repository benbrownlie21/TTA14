import requests, json, psycopg2

country_api_json = requests.get("https://restcountries.com/v3.1/all").json()

conn = psycopg2.connect(
    database="dailychallenge",
    user="postgres",
    password="New2020Road!",
    host="localhost",
    port="5433",
)

conn.autocommit = True
cursor = conn.cursor()

for country_api in country_api_json:
    data = json.dumps(country_api)
    insert_query = "INSERT INTO rest_countries (country_info) values (%s)"
    cursor.execute(insert_query, (data,))

conn.commit()
conn.close()
