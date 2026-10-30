from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from db.connection import get_db
from models.application import Application
from schemas.application import ApplicationCreate

app = FastAPI(title="Job Tracker API")

@app.get("/")
def home():
    return {"message": "Job Tracker API is running"}

@app.get("/api/applications")
def get_applications(db: Session = Depends(get_db)):
    applications = db.query(Application).all()

    return {
        "applications": [
            {
                "id": app.id,
                "company": app.company,
                "role": app.role,
                "status": app.status
            }
            for app in applications
        ]
    }

@app.post("/api/applications")
def create_application(
    data: ApplicationCreate,
    db: Session = Depends(get_db)
):
    application = Application(
        user_id=data.user_id,
        company=data.company,
        role=data.role,
        status=data.status
    )

    db.add(application)
    db.commit()
    db.refresh(application)

    return {
        "message": "Application created successfully",
        "application": {
            "id": application.id,
            "user_id": application.user_id,
            "company": application.company,
            "role": application.role,
            "status": application.status
        }
    }