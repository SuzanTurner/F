from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import dotenv
import os

dotenv.load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:SzrdWabVtBjKqxWVXrCgSlKzGMmiHdRA@shortline.proxy.rlwy.net:14190/railway")

engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind = engine, autocommit = False, autoflush=  False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()