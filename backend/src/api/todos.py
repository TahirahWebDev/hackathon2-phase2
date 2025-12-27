from fastapi import APIRouter, Depends, HTTPException, status, Path, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlmodel import Session
from typing import List
from ..database.database import get_session
from ..models.todo import Todo
from ..services.todo_service import TodoService
from ..services.auth_service import AuthService
from ..api.models.responses import TodoResponse
from pydantic import BaseModel
from datetime import datetime
import jwt
from jose import JWTError
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

router = APIRouter()

# Security scheme for Bearer token
security = HTTPBearer()

class TodoCreateRequest(BaseModel):
    title: str
    description: str = None
    completed: bool = False


class TodoUpdateRequest(BaseModel):
    title: str = None
    description: str = None
    completed: bool = None


def get_current_user_id(credentials: HTTPAuthorizationCredentials = Security(security)):
    """Get the current user ID from the JWT token."""
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        return user_id
    except JWTError:
        raise credentials_exception


@router.get("/", response_model=List[TodoResponse])
def get_todos(
    session: Session = Depends(get_session),
    current_user_id: int = Security(get_current_user_id)
):
    todos = TodoService.get_todos_by_user(session, current_user_id)
    return todos


@router.post("/", response_model=TodoResponse)
def create_todo(
    request: TodoCreateRequest,
    session: Session = Depends(get_session),
    current_user_id: int = Security(get_current_user_id)
):
    todo = TodoService.create_todo(
        session=session,
        title=request.title,
        description=request.description,
        user_id=current_user_id
    )
    return todo


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: int = Path(..., title="The ID of the todo"),
    session: Session = Depends(get_session),
    current_user_id: int = Security(get_current_user_id)
):
    todo = TodoService.get_todo_by_id(session, todo_id, current_user_id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    return todo


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(
    request: TodoUpdateRequest,
    todo_id: int = Path(..., title="The ID of the todo"),
    session: Session = Depends(get_session),
    current_user_id: int = Security(get_current_user_id)
):
    todo = TodoService.update_todo(
        session=session,
        todo_id=todo_id,
        user_id=current_user_id,
        title=request.title,
        description=request.description,
        completed=request.completed
    )
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    return todo


@router.patch("/{todo_id}/toggle", response_model=TodoResponse)
def toggle_todo(
    todo_id: int = Path(..., title="The ID of the todo"),
    session: Session = Depends(get_session),
    current_user_id: int = Security(get_current_user_id)
):
    todo = TodoService.toggle_todo_completion(session, todo_id, current_user_id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    return todo


@router.delete("/{todo_id}")
def delete_todo(
    todo_id: int = Path(..., title="The ID of the todo"),
    session: Session = Depends(get_session),
    current_user_id: int = Security(get_current_user_id)
):
    success = TodoService.delete_todo(session, todo_id, current_user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    return {"message": "Todo deleted successfully"}