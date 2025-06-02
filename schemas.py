from pydantic import BaseModel
import datetime

class respect(BaseModel):
    id: int
    ip : int
    country : str
    state : str
    timestamp : datetime.datetime
    
    class Config:
        orm_mode = True