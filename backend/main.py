from fastapi import FastAPI

app = FastAPI(title="Job Tracker API")

@app.get("/")
def home():
    return {"message": "Job Tracker API is running"}
