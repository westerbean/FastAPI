from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://postgres:{settings.secret_key}@{settings.database_hostname}:{settings.database_port}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:

#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Brbquick1',
#                                 cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connected successfully!")
#         break

#     except Exception as error:
#         print("Database connection unsuccessful!")
#         print("Error:", error)
#         time.sleep(2)