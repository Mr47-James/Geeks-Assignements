import requests
import psycopg2
import random

# ------------------------
# DATABASE CONNECTION
# ------------------------
def connect_db():
    return psycopg2.connect(
        dbname="countries_db",
        user="postgres",
        password="yourpassword",
        host="localhost",
        port="5432"
    )

# ------------------------
# DATABASE SETUP
# ------------------------
def create_countries_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            capital VARCHAR(100),
            flag TEXT,
            subregion VARCHAR(100),
            population BIGINT
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

# ------------------------
# FETCH COUNTRIES FROM API
# ------------------------
def fetch_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching countries:", response.status_code)
        return []

# ------------------------
# INSERT RANDOM COUNTRIES INTO DB
# ------------------------
def insert_random_countries(n=10):
    countries = fetch_countries()
    if not countries:
        return

    selected_countries = random.sample(countries, n)

    conn = connect_db()
    cur = conn.cursor()

    for country in selected_countries:
        name = country.get("name", {}).get("common", "Unknown")
        capital_list = country.get("capital", [])
        capital = capital_list[0] if capital_list else None
        flag = country.get("flags", {}).get("png", None)
        subregion = country.get("subregion", None)
        population = country.get("population", None)

        cur.execute("""
            INSERT INTO countries (name, capital, flag, subregion, population)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, capital, flag, subregion, population))

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Inserted {n} random countries into the database.")

# ------------------------
# RUN
# ------------------------
if __name__ == "__main__":
    create_countries_table()
    insert_random_countries()
