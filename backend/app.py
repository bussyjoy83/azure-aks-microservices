import os
import time
import psycopg2
from flask import Flask, jsonify
 
app = Flask(__name__)
 
DB_HOST = os.getenv("DB_HOST", "postgres")
DB_NAME = os.getenv("DB_NAME", "shoestore")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
 
def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        connect_timeout=5
    )
 
def wait_for_db(retries=10, delay=5):
    for i in range(retries):
        try:
            conn = get_connection()
            conn.close()
            print("Database ready")
            return
        except Exception as e:
            print(f"Waiting for DB ({i+1}/{retries})...")
            time.sleep(delay)
    raise Exception("Database not ready")
 
def init_db():
    conn = get_connection()
    cur = conn.cursor()
    # create tables here
    conn.commit()
    cur.close()
    conn.close()
 
@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200
 
# RUN ON IMPORT (Gunicorn-safe)
wait_for_db()
init_db()

