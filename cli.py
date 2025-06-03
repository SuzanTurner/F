
import requests
import dotenv
import os
import json
import datetime
# from user import ip, country, state, timestamp

dotenv.load_dotenv()
BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
# print(BASE_URL)

parameters = {"access_key" : API_KEY, }
resp = requests.get(url = API_URL, params = parameters)
data = resp.json()

ip = data.get("ip")
country = data.get("country_name")
state = data.get("region_name")
timestamp = datetime.datetime.now(datetime.UTC).isoformat()

resp = requests.get(BASE_URL)
print("\n--- Home Route ---")
print(json.dumps(resp.json(), indent=2))

while True:
    inp = input("Press F to pay respect: ").strip()
    timestamp = datetime.datetime.now(datetime.UTC).isoformat()
    
    if inp == 'F':
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
