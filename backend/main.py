from fastapi import FastAPI
from db.connection import engine, Base
import models  # registers the tables

Base.metadata.create_all(bind=engine)

app = FastAPI(title="JobTracker API")

@app.get("/")
def home():
    return {"message": "JobTracker API is running"}