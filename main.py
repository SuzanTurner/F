from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from db import engine, get_db
from sqlalchemy.orm import Session
import models
import schemas
import datetime
import uvicorn

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post("/F")
async def send_respect(request : schemas.Respect,  db : Session = Depends(get_db)):
    new_user = models.respect(ip = request.ip, country = request.country, state = request.state, timestamp = request.timestamp)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": f"User with IP Address {request.ip} from {request.country} {request.state} sent respect at {request.timestamp}"}

@app.get("/f")
async def send_respect():
    return {"message": "Bro Press F! For RESPECT!"}

@app.get("/")
async def send_respect():
    return JSONResponse(
        status_code=200,           
        content = {"command": "Click PrettyPrint",
            "about me" :"I am Yadh \nI code python \nI lay in the Backends",
            "some info" : "I don't fw html/js",
            "message" : "Press F to pay respect"}
        ) 
 
@app.get("/{anything_else}")
async def bro_press_f(anything_else: str):
    return JSONResponse(
        status_code=400,
        content={"message": "bro press F"}
    )
    
@app.get("/log")
async def view_log(db : Session = Depends(get_db)):
    users = db.query(models.respect).all()
    return users
    
if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8080)