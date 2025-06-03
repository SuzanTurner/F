
import requests
import dotenv
import os
import json
from datetime import datetime
import pytz
# from user import ip, country, state, timestamp

dotenv.load_dotenv()
# BASE_URL = os.getenv("BASE_URL")
# API_KEY = os.getenv("API_KEY")
# API_URL = os.getenv("API_URL")

BASE_URL = "http://f-production-2a80.up.railway.app"
# BASE_URL = "http://localhost:8000"
# API_KEY = "641549f1e6dc09ff8ec7f3aa292d8e9a"
# API_URL = "http://api.ipstack.com/check"
# print(BASE_URL)

TOKEN = "b333f695b06323"
API_URL = "https://ipinfo.io/json" 
parameters = {"token": TOKEN}

resp = requests.get(url=API_URL, params=parameters)
data = resp.json()

ip = data.get("ip")
country = data.get("country")
state = data.get("region")

print("\n--- Geolocation Info ---")
print(json.dumps({
    "ip": ip,
    "country": country,
    "state": state
}, indent=2))

resp = requests.get(f"{BASE_URL}")
print(json.dumps(resp.json(), indent=2))

while True: 
    inp = input("Press F to pay respect: ").strip()      
    
    if inp == 'F':

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
        
        ip = data.get("ip")
        country = data.get("country")
        state = data.get("region")
        
        print("Sending respect with:", {
        "ip": ip,
    "country": country,
    "state": state,
    "timestamp": timestamp
})
        try:
            resp = requests.post(
                f"{BASE_URL}/F",
                json={
                    "ip": ip,
                    "country": country,
                    "state": state,
                    "timestamp": timestamp
                }
            )
            resp.raise_for_status()
            print(json.dumps(resp.json(), indent=2))
            break
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            if hasattr(e.response, 'text'):
                print("Server response:", e.response.text)
            break
    elif inp == 'f':
        resp = requests.get(f"{BASE_URL}/f")
        print(json.dumps(resp.json(), indent=2))
    else:
        resp = requests.get(f"{BASE_URL}/{inp}")
        print(json.dumps(resp.json(), indent=2))
