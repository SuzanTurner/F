from sqlalchemy import Column, Integer, String
from db import Base

class respect(Base):
    __tablename__ = "Respects"
    
    id = Column(Integer, primary_key=True, index= True)
    ip = Column(String, nullable = False)
    country = Column(String, nullable = False)
    state = Column(String, nullable = False)
    timestamp = Column(String, nullable = False)
    