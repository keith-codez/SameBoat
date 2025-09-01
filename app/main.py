# app/main.py
import time
import os
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

from app.database import Base 
from app.routes import faqs, blogs
from . import models  # Your SQLAlchemy models

# Load DB environment variables
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "samboat")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, echo=True)

app = FastAPI()

# Include routers
app.include_router(faqs.router)
app.include_router(blogs.router)



def wait_for_db(retries=10, delay=3):
    """Retry connecting to the DB until it succeeds or runs out of retries."""
    attempt = 0
    while attempt < retries:
        try:
            # Try to connect and reflect tables
            with engine.connect() as conn:
                print("Database connected!")
            return
        except OperationalError:
            attempt += 1
            print(f"Database not ready, retrying ({attempt}/{retries})...")
            time.sleep(delay)
    raise Exception("Could not connect to the database after several attempts.")


@app.on_event("startup")
def on_startup():
    # Wait for Postgres to be ready
    wait_for_db()

    # Create tables
    Base.metadata.create_all(bind=engine)
    print("Tables created or verified!")
