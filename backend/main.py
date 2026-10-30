from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from db.connection import get_db
from models.application import Application
from schemas.application import ApplicationCreate,ApplicationUpdate
from fastapi import HTTPException

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

@app.update("/api/application/{application_id}")
def update_application(
    application_id: int,
    data: ApplicationUpdate,
    db: Session = Depends(get_db)
):
    application = db.query(Application).filter(
        Application.id == application_id
    ).first()
    if application is None:
        raise HTTPException(
            status_code= 404,
            detail = "Application not found"
        )
    if application is not None :
        application.status = data.status

    db.commit()
    db.refresh(application)

    return {
        "message" : "Application Update sucessfully",
        "application": {
            "id": application.id,
            "company": application.company,
            "role": application.role,
            "status": application.status
        }
    }

@app.delete("/api/application/{application_id}")
def delete_application(
    application_id: int,
    db: Session = Depends(get_db)
):
    application = db.query(Application).filter(
        Application.id == application_id
    ).first()

    if application is None:
        raise HTTPException(
            status_code = 404,
            detail = "Application Not Found"
        )
    db.delete(application)
    db.commit()

    return{
        "message": "Application deleted sucessfully"
    }