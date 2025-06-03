import dotenv
import os
import requests
from datetime import datetime
import pytz

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
API_URL = os.getenv("API_URL")
# FASTAPI_URL = os.getenv("FASTAPI_URL")
# FASTAPI_URL = "http://127.0.0.1:8000/F"

parameters = {"token": TOKEN}

resp = requests.get(url=API_URL, params=parameters)
data = resp.json()

ip = data.get("ip")
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
            

user_info = {
    "ip": ip,
    "country": country,
    "state": state,
    "timestamp": timestamp
}

# print(f"Data to send: IP={ip}, Country={country}, State={state}, Timestamp={timestamp}")


