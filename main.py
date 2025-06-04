from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from db import engine, get_db
from sqlalchemy.orm import Session
import models
import schemas
import uvicorn
from sqlalchemy.exc import SQLAlchemyError
import logging
from user import ip, country, state, timestamp
 # use uvicorn's logger for visibility


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


try:
    models.Base.metadata.create_all(engine)
    logger.info("Database tables created successfully")
except SQLAlchemyError as e:
    logger.error(f"Error creating database tables: {e}")
    raise

logger.info("🚀 App just started on Railway!")

@app.post("/F")
async def send_respect(request : schemas.respect,  db : Session = Depends(get_db)):
    logger.info(f"🔥 POST BODY RECEIVED: {request.dict()}")
    print("🔥 POST BODY RECEIVED:", request.dict())

    new_user = models.respect(
        ip = request.ip,
        country = request.country,
        state = request.state,
        timestamp = request.timestamp
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": f"User with IP Address {request.ip} from {request.country}, {request.state} sent respect at {request.timestamp}"}
    
@app.get("/F")
async def send_respect_from_browser(request: Request, db: Session = Depends(get_db)):
    logger.info(f"🔥 GET BODY RECEIVED: {Request}")
    print("🔥 GET BODY RECEIVED:", Request)
    
    new_user = models.respect(
        ip=ip,
        country=country,
        state=state,
        timestamp=timestamp
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": f"User with IP Address {ip} from {country}, {state} sent respect at {timestamp}"}



@app.get("/f")
async def send_respect():
    return {"message": "Bro Press F! For RESPECT!"}

@app.get("/")
async def root():
    return JSONResponse(
        status_code=200,           
        content = {
            "command": "Click PrettyPrint",
            "about me": "I am Yadh \nI code python \nI lay in the Backends",
            "some info": "I don't fw html/js",
            "message": "Press F to pay respect"
        }
    ) 
    
@app.get("/log")
async def view_log(db : Session = Depends(get_db)):
    try:
        users = db.query(models.respect).all()
        return users
    except SQLAlchemyError as e:
        logger.error(f"Error fetching logs: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching logs: {str(e)}")

@app.get("/{anything_else}")
async def bro_press_f(anything_else: str):
    return JSONResponse(
        status_code=400,
        content={"message": "bro press F"}
    )
    
@app.get("/debug")
def debug():
    logger.info("Debug route was hit!")
    return {"msg": "Logged successfully!"}

if __name__ == "__main__":
    logger.info("Starting application...")
    uvicorn.run("main:app", host = "0.0.0.0", port = 8000, reload = False)