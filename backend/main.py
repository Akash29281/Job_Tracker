from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from db.connection import get_db
from models.application import Application
from schemas.application import ApplicationCreate,ApplicationUpdate
from fastapi import HTTPException
from schemas.user import UserCreate, Userlogin
from models.user import User
from core.security import hash_password, verify_password
from core.token import create_access_token

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

@app.patch("/api/application/{application_id}")
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

@app.post("/api/auth/register")
def register_user(
    data: UserCreate,
    db: Session = Depends(get_db)

):
    # Check if email already exists
    existing_user = db.query(User).filter(
        User.email == data.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code = 404,
            detail="Email already registered"
        )
    #hash Password
    hashed_password = hash_password(data.password)

    #Create new user
    new_user = User(
        name = data.name,
        email = data.email,
        password_hash = hashed_password
    )

    # Save user in database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered sucessfully",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        }
    }

@app.post("/api/auth/login")
def login_user(
        data: Userlogin,
        db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.email == data.email
    ).first()

    if user is None:
        raise HTTPException(
            status_code = 401,
            detail="Invalid email or password"
        )
    if not verify_password(data.password, user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    access_token = create_access_token(user.id)

    return{
        "message": "Login Sucessfully",
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }