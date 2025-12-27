import os
from sqlmodel import Session, create_engine, text
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
# Clean quotes if they exist
if DATABASE_URL:
    DATABASE_URL = DATABASE_URL.strip("'").strip('"')

engine = create_engine(DATABASE_URL)

def verify_tables():
    with Session(engine) as session:
        print("--- Checking Neon Database Schema ---")
        try:
            # Check if user table exists
            result = session.exec(text("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'user'")).all()
            if not result:
                print("❌ ERROR: Table 'user' does not exist in Neon!")
            else:
                print("✅ Table 'user' found. Columns:")
                for col in result:
                    print(f"   - {col[0]} ({col[1]})")
        except Exception as e:
            print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    verify_tables()