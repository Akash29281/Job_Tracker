from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class ApplicationCreate(BaseModel):
    user_id: int
    company: str = Field(min_length=1, max_length=100)
    role: str = Field(min_length=1, max_length=100)
    status: str = "applied"



class ApplicationStatus(str, Enum):
    APPLIED = "applied"
    UNDER_REVIEW = "under_review"
    INTERVIEW = "interview"
    SELECTED = "selected"
    REJECTED = "rejected"
    OFFER_RECEIVED = "offer_received"
    WITHDRAWN = "withdrawn"


class ApplicationCreate(BaseModel):
    user_id: int
    company: str = Field(min_length=1, max_length=100)
    role: str = Field(min_length=1, max_length=100)
    status: ApplicationStatus = ApplicationStatus.APPLIED


class ApplicationUpdate(BaseModel):
    status: Optional[ApplicationStatus] = None

