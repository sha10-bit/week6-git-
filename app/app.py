from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# PostgreSQL connection
DB_HOST = os.environ.get("POSTGRES_HOST", "db")
DB_NAME = os.environ.get("POSTGRES_DB", "testdb")
DB_USER = os.environ.get("POSTGRES_USER", "admin")
DB_PASS = os.environ.get("POSTGRES_PASSWORD", "admin123")

def get_db_version():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return version
    except Exception as e:
        return str(e)

@app.route("/")
def home():
    return f"Hello! Connected to DB: {get_db_version()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
