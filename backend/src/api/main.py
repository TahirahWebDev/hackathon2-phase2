from fastapi import FastAPI, Request
import traceback
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .auth import router as auth_router
from .todos import router as todos_router
from ..models.user import User 
from ..models.todo import Todo
from sqlmodel import SQLModel
from ..database.database import engine

app = FastAPI(title="Todo API", version="0.1.0", redirect_slashes=False)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include routers
app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(todos_router, prefix="/api/todos", tags=["todos"])

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}

@app.exception_handler(Exception)
async def debug_exception_handler(request: Request, exc: Exception):
    # This will print the exact line causing the crash in your terminal
    print("".join(traceback.format_exception(type(exc), exc, exc.__traceback__)))
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc), "type": str(type(exc))}
    )