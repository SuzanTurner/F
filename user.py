import dotenv
import os
import requests
import datetime

dotenv.load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
# FASTAPI_URL = os.getenv("FASTAPI_URL")
# FASTAPI_URL = "http://127.0.0.1:8000/F"

parameters = {"access_key" : API_KEY, }
resp = requests.get(url = API_URL, params = parameters)
data = resp.json()

ip = data.get("ip")
country = data.get("country_name")
state = data.get("region_name")
timestamp = datetime.datetime.now(datetime.UTC).isoformat()

user_info = {
    "ip": ip,
    "country": country,
    "state": state,
    "timestamp": timestamp
}

# print(f"Data to send: IP={ip}, Country={country}, State={state}, Timestamp={timestamp}")


