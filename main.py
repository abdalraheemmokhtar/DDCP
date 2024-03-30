import os
from dotenv import load_dotenv
from fastapi import FastAPI
from databases import Database
from sqlalchemy import create_engine

load_dotenv()

app = FastAPI()
database = Database(
    f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)
metadata = create_engine(
    f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
@app.get("/")
async def fetch_data():
    query = "SELECT * FROM core_post;"
    results = await database.fetch_all(query)
    return {"data": results}
