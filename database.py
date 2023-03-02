from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

# Create a mysql engine instance
DATABASE_URL = "mysql+mysqlconnector://root:Admin@2022@localhost:3306/empdb"

engine = create_engine(DATABASE_URL)

# Create a DeclarativeMeta instance
Base = declarative_base()

# Create SessionLocal class from sessionmaker factory
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()