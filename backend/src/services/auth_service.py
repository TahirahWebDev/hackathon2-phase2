from datetime import datetime, timedelta
from typing import Optional
from sqlmodel import Session
from sqlmodel import select
from passlib.context import CryptContext
from jose import JWTError, jwt
from ..models.user import User
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT settings
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))


class AuthException(Exception):
    """Custom exception for authentication errors"""
    pass


class AuthService:
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify a plain password against a hashed password."""
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        """Generate a hash for a plain password."""
        return pwd_context.hash(password)

    @staticmethod
    @staticmethod
    def authenticate_user(session: Session, email: str, password: str) -> Optional[User]:
    # Use select instead of session.query
       statement = select(User).where(User.email == email)
       user = session.exec(statement).first() # Use exec for SQLModel sessions
    
       if not user or not AuthService.verify_password(password, user.hashed_password):
            return None
       return user

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        """Create a JWT access token."""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt