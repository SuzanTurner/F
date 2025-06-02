from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/F")
async def send_respect():
    return {"message": "Respect sent!"}

@app.get("/f")
async def send_respect():
    return {"message": "Bro Press F! For RESPECT!"}

@app.get("/")
async def send_respect():
    return {"command": "Click PrettyPrint",
            "about me" :"I am Yadh \nI code python \nI lay in the Backends",
            "some info" : "I don't fw html/js",
            "message" : "Press F to pay respect (obv in the url)"}
 
@app.get("/{anything_else}")
async def bro_press_f(anything_else: str):
    return JSONResponse(
        status_code=400,
        content={"message": "bro press F"}
    )
    
if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8080)