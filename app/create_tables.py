# app/create_tables.py
from .database import Base, engine
from . import models  # this imports your FAQ model

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
