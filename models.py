from sqlalchemy import Column, Integer, String, DateTime
import datetime
from db import Base

class respect(Base):
    __tablename__ = "Respects"
    
    id = Column(Integer, primary_key=True, index= True)
    ip = Column(Integer, nullable = False)
    country = Column(String, nullable = False)
    state = Column(String, nullable = False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)