from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):  
    title: str
    description: Optional[str] = None
    completed: bool = False
    
    @field_validator('title')
    @classmethod
    def title_must_not_be_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError('Title cannot be empty')
        return v

class TaskRead(BaseModel):
    id: int
    title: str
    description: Optional[str]
    owner_id: int
    completed: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True