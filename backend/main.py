from fastapi import FastAPI

app = FastAPI(title="JobTracker API")

@app.get("/")
def home():
    return {"message": "JobTracker API is Running.."}