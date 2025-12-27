from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from datetime import timedelta
from ..database.database import get_session
from ..services.auth_service import AuthService, AuthException
from ..services.user_service import UserService
from ..api.models.responses import TokenResponse, UserResponse
from pydantic import BaseModel
from ..services.auth_service import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()


class SignUpRequest(BaseModel):
    email: str
    password: str


class SignInRequest(BaseModel):
    email: str
    password: str


@router.post("/signup", response_model=UserResponse)
def signup(request: SignUpRequest, session: Session = Depends(get_session)):
    """Register a new user."""
    try:
        user = UserService.create_user(
            session=session,
            email=request.email,
            password=request.password
        )

        # Return basic user info without sensitive data
        return UserResponse(
            id=user.id,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during registration"
        )


@router.post("/signin", response_model=TokenResponse)
def signin(request: SignInRequest, session: Session = Depends(get_session)):
    """Authenticate an existing user."""
    user = AuthService.authenticate_user(
        session=session,
        email=request.email,
        password=request.password
    )
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=AuthService.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = AuthService.create_access_token(
        data={"sub": user.email, "user_id": user.id}, 
        expires_delta=access_token_expires
    )
    
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user={
            "id": user.id,
            "email": user.email
        }
    )


@router.post("/signout")
def signout():
    """Log out the current user."""
    # In a real implementation, you might want to add the token to a blacklist
    # For now, we just return a success message
    return {"message": "Successfully logged out"}