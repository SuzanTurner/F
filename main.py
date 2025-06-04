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
import os
from datetime import datetime
import pytz
import requests
# from user import ip, country, state, timestamp
# use uvicorn's logger for visibility


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*", "Content-Type", "application/json"]
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
    logger.info(f"🔥 POST BODY RECEIVED: {request.model_dump()}")
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
    logger.info(f"🔥 GET BODY RECEIVED: {request}")
    print("🔥 GET BODY RECEIVED:", request)
    '''
    new_user = models.respect(
        ip=request.ip,
        country=request.country,
        state=request.state,
        timestamp=request.timestamp
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    '''
    try: 
        forwarded = request.headers.get("X-Forwarded-For")
        ip = forwarded.split(",")[0].strip() if forwarded else request.client.host

        TOKEN = "b333f695b06323"
        API_URL = "https://ipinfo.io/json" 
        parameters = {"token": TOKEN}

        resp = requests.get(url=API_URL, params=parameters)
        data = resp.json()

        TOKEN = "b333f695b06323"
        API_URL = f"https://ipinfo.io/{ip}/json"
        
        resp = requests.get(API_URL, params={"token": TOKEN})
        data = resp.json()

        country = data.get("country")
        state = data.get("region")
        
        india = pytz.timezone("Asia/Kolkata")
        ist_time = datetime.now(india)

        day = ist_time.day
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]

        month = ist_time.strftime("%B")  

        hour_24 = ist_time.hour
        hour_12 = hour_24 % 12 or 12        
        minute = ist_time.minute

        ampm = "pm" if hour_24 >= 12 else "am"

        timestamp = f"{day}{suffix} {month} {hour_12}:{minute:02d} {ampm}"
        
        logger.info(ip, country, state, timestamp)
        
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
        # return {"message" : "Respect Sent!"}
    except Exception as e:
        return {"Couldn't send respect... "}

'''
@app.get("/F")
async def send_respect_from_browser(db: Session = Depends(get_db)):
    
    logger.info("IN GET/F")
    
    import requests
    TOKEN = "b333f695b06323"  
    API_URL = "https://ipinfo.io/json"
    
    response = requests.get(API_URL, params={"token": TOKEN})
    data = response.json()
    
    ip = data.get("ip")
    country = data.get("country")
    state = data.get("region")

    
    from datetime import datetime
    import pytz
    
    india = pytz.timezone("Asia/Kolkata")
    ist_time = datetime.now(india)

    day = ist_time.day
    suffix = "th" if 4 <= day <= 20 or 24 <= day <= 30 else ["st", "nd", "rd"][day % 10 - 1]
    month = ist_time.strftime("%B")  
    hour_12 = ist_time.hour % 12 or 12
    minute = ist_time.minute
    ampm = "PM" if ist_time.hour >= 12 else "AM"

    timestamp = f"{day}{suffix} {month} {hour_12}:{minute:02d} {ampm}"

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
'''

@app.get("/f")
async def send_respect():
    logger.info(f"🔥 INSIDE /f GET ENDPOINT")
    print("🔥 INSIDE /f GET ENDPOINT")
    return {"message": "Bro Press F! For RESPECT!"}

@app.get("/")
async def root():
    logger.info("HOME ROUTE")
    return JSONResponse(
        status_code=200,           
        content = {
            "command": "Click PrettyPrint",
            "about me": "I am Yadh. I code python. I lay in the Backends",
            "some info": "I don't fw html/js",
            "what is this?" : "This is a simple cli thingi I made. I was bored",
            "message": "Press F to pay respect"
        }
    ) 
    
@app.get("/log")
async def view_log(db : Session = Depends(get_db)):
    logger.info("INSIDE /log ENDPOINT")
    print("INSIDE /log ENDPOINT")
    try:
        users = db.query(models.respect).all()
        return users
    except SQLAlchemyError as e:
        logger.error(f"Error fetching logs: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching logs: {str(e)}")
    
@app.get("/headers")
async def get_headers(request: Request):
    return dict(request.headers)

@app.get("/check")
async def get_ip(request: Request):
    forwarded = request.headers.get("X-Forwarded-For")
    ip = forwarded.split(",")[0].strip() if forwarded else request.client.host
    return {"ip": ip}

@app.get("/{anything_else}")
async def bro_press_f(anything_else: str):
    if anything_else == "favicon.ico":  
        return JSONResponse(status_code=404, content={"message": "favicon request"})
    logger.info("ANYTING ELSE WAS PRESSED")
    print("ANYTHING ELSE WAS PRESSED")
    return JSONResponse(
        status_code=400,
        content={"message": "bro press F"}
    )
    
if __name__ == "__main__":
    logger.info("Starting application...")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)