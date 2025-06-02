from pydantic import BaseModel
from datetime import datetime

class respect(BaseModel):
    ip : str
    country : str
    state : str
    timestamp : datetime
    
    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }