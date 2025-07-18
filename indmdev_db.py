import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    conn = psycopg2.connect(
        host=os.getenv('DATABASE_HOST'),
        database=os.getenv('DATABASE_NAME'),
        user=os.getenv('DATABASE_USER'),
        password=os.getenv('DATABASE_PASSWORD'),
        port=os.getenv('DATABASE_PORT')
    )
    return conn

def log_alert(symbol, signal_type, entry, sl, tp, timestamp):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO alerts (symbol, signal_type, entry, stop_loss, take_profit, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (symbol, signal_type, entry, sl, tp, timestamp))
    conn.commit()
    cursor.close()
    conn.close()
