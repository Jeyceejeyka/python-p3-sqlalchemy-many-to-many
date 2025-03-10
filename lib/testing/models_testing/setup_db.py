from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # Ensure models.py defines `Base`

# ✅ Ensure the correct database file name
engine = create_engine("sqlite:///many_to_many.db")  # Use the correct database file

# ✅ Create all tables defined in models.py
Base.metadata.create_all(engine)

print("✅ Database tables created successfully!")
