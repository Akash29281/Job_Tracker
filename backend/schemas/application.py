from pydantic import BaseModel, Field


class ApplicationCreate(BaseModel):
    user_id: int
    company: str = Field(min_length=1, max_length=100)
    role: str = Field(min_length=1, max_length=100)
    status: str = "applied"