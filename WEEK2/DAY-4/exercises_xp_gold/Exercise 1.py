import psycopg2
from psycopg2 import sql
import bcrypt

# ------------------------
# DATABASE CONNECTION
# ------------------------
def connect_db():
    return psycopg2.connect(
        dbname="authentication_db",
        user="postgres",
        password="yourpassword",
        host="localhost",
        port="5432"
    )

# ------------------------
# DATABASE SETUP
# ------------------------
def create_users_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

# ------------------------
# USER MANAGEMENT FUNCTIONS
# ------------------------
def add_user(username, password):
    conn = connect_db()
    cur = conn.cursor()
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_pw))
        conn.commit()
        print("[*] User signed up successfully.")
    except psycopg2.IntegrityError:
        conn.rollback()
        print("[*] Username already exists.")
    finally:
        cur.close()
        conn.close()

def authenticate_user(username, password):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    if result and bcrypt.checkpw(password.encode(), result[0].encode()):
        return True
    return False

# ------------------------
# CLI INTERFACE
# ------------------------
def main():
    create_users_table()
    logged_in = None

    while True:
        action = input("\nEnter 'login', 'signup', or 'exit': ").lower()

        if action == "exit":
            print("[*] Goodbye!")
            break

        elif action == "login":
            username = input("Username: ")
            password = input("Password: ")
            if authenticate_user(username, password):
                print(" You are now logged in.")
                logged_in = username
            else:
                print("[*] Invalid username or password.")

        elif action == "signup":
            while True:
                username = input("Choose a username: ")
                conn = connect_db()
                cur = conn.cursor()
                cur.execute("SELECT * FROM users WHERE username = %s", (username,))
                exists = cur.fetchone()
                cur.close()
                conn.close()
                if exists:
                    print("[*] Username already taken. Try again.")
                else:
                    break
            password = input("Choose a password: ")
            add_user(username, password)

        else:
            print("[*] Invalid command. Please enter 'login', 'signup', or 'exit'.")

if __name__ == "__main__":
    main()
