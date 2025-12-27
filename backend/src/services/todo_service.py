from sqlmodel import Session, select
from typing import List, Optional
from ..models.todo import Todo
from ..models.user import User


class TodoService:
    """Service class for todo operations"""
    
    @staticmethod
    def create_todo(session: Session, title: str, description: Optional[str], user_id: int) -> Todo:
        """Create a new todo for a user."""
        todo = Todo(
            title=title,
            description=description,
            user_id=user_id
        )
        
        session.add(todo)
        session.commit()
        session.refresh(todo)
        
        return todo

    @staticmethod
    def get_todos_by_user(session: Session, user_id: int) -> List[Todo]:
        """Get all todos for a specific user."""
        statement = select(Todo).where(Todo.user_id == user_id)
        todos = session.exec(statement).all()
        return todos

    @staticmethod
    def get_todo_by_id(session: Session, todo_id: int, user_id: int) -> Optional[Todo]:
        """Get a specific todo by ID for a specific user."""
        statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
        todo = session.exec(statement).first()
        return todo

    @staticmethod
    def update_todo(
        session: Session, 
        todo_id: int, 
        user_id: int, 
        title: Optional[str] = None, 
        description: Optional[str] = None, 
        completed: Optional[bool] = None
    ) -> Optional[Todo]:
        """Update a specific todo for a user."""
        todo = TodoService.get_todo_by_id(session, todo_id, user_id)
        if not todo:
            return None
        
        # Update fields if provided
        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description
        if completed is not None:
            todo.completed = completed
        
        session.add(todo)
        session.commit()
        session.refresh(todo)
        
        return todo

    @staticmethod
    def toggle_todo_completion(session: Session, todo_id: int, user_id: int) -> Optional[Todo]:
        """Toggle the completion status of a specific todo for a user."""
        todo = TodoService.get_todo_by_id(session, todo_id, user_id)
        if not todo:
            return None
        
        todo.completed = not todo.completed
        
        session.add(todo)
        session.commit()
        session.refresh(todo)
        
        return todo

    @staticmethod
    def delete_todo(session: Session, todo_id: int, user_id: int) -> bool:
        """Delete a specific todo for a user."""
        todo = TodoService.get_todo_by_id(session, todo_id, user_id)
        if not todo:
            return False
        
        session.delete(todo)
        session.commit()
        return True