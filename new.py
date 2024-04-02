from fastapi import FastAPI
import psycopg2

app = FastAPI()
def get_db_conn():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="Fast",
        user="postgres",
        password="root"
    )
    return conn

@app.get("/users")
def get_users():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return {"users": users}