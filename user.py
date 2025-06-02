import dotenv
import os
import requests
import datetime

dotenv.load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
FASTAPI_URL = os.getenv("FASTAPI_URL")

parameters = {"access_key" : API_KEY, }
resp = requests.get(url = API_URL, params = parameters)
data = resp.json()

# Extracting details
ip = data.get("ip")
country = data.get("country_name")
state = data.get("region_name")
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(ip, country, state, timestamp)
print(FASTAPI_URL)

response = requests.post(
    FASTAPI_URL,
    json={
        "ip": ip,
        "country": country,
        "state": state,
        "timestamp": timestamp
    }
)

try:
    print("Response:", response.json())
except:
    print("Raw Response:", response.text)


