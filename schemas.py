from pydantic import BaseModel

class respect(BaseModel):
    ip : str
    country : str
    state : str
    timestamp : str
    
