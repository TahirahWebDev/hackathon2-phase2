from sqlmodel import create_engine, Session, SQLModel
from typing import Generator
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the engine
engine = create_engine(
    DATABASE_URL, 
    pool_recycle=300,   # Refreshes the connection every 5 minutes
    pool_pre_ping=True,  # Checks if the connection is alive before using it
    echo=True
)


def create_db_and_tables():
    """Create database tables for all models."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """Get a database session."""
    with Session(engine) as session:
        yield session