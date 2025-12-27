from fastapi import Request, HTTPException, status
from fastapi.security.http import HTTPBearer, HTTPCredentials
from jose import jwt
from functools import wraps
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

security = HTTPBearer()


class AuthMiddleware:
    """Authentication middleware to verify JWT tokens."""
    
    @staticmethod
    async def verify_token(token: str):
        """Verify the JWT token and return user ID if valid."""
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id: int = payload.get("user_id")
            if user_id is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Could not validate credentials",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            return user_id
        except jwt.JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

    @staticmethod
    def require_auth():
        """Decorator to require authentication for specific routes."""
        async def auth_wrapper(request: Request):
            # Get the authorization header
            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Bearer "):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Authorization header missing or invalid",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            
            # Extract the token
            token = auth_header.split(" ")[1]
            
            # Verify the token
            user_id = await AuthMiddleware.verify_token(token)
            
            # Add user ID to request state for use in route handlers
            request.state.user_id = user_id
            
            return user_id
        
        return auth_wrapper