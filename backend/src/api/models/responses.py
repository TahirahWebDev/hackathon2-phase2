from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: dict


class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    user_id: int
    created_at: datetime
    updated_at: datetime


class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
    updated_at: datetime