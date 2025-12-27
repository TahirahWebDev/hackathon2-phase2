from sqlmodel import Session, select
from typing import Optional
from ..models.user import User
from .auth_service import AuthService


class UserService:
    """Service class for user operations"""
    
    @staticmethod
    def create_user(session: Session, email: str, password: str) -> User:
        """Create a new user with hashed password."""
        # Check if user already exists
        existing_user = session.query(User).filter(User.email == email).first()
        if existing_user:
            raise ValueError("User with this email already exists")
        
        # Hash the password
        hashed_password = AuthService.get_password_hash(password)
        
        # Create the new user
        user = User(
            email=email,
            hashed_password=hashed_password
        )
        
        # Add to session and commit
        session.add(user)
        session.commit()
        session.refresh(user)
        
        return user

    @staticmethod
    def get_user_by_email(session: Session, email: str) -> Optional[User]:
        """Get a user by their email."""
        statement = select(User).where(User.email == email)
        user = session.exec(statement).first()
        return user

    @staticmethod
    def get_user_by_id(session: Session, user_id: int) -> Optional[User]:
        """Get a user by their ID."""
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).first()
        return user