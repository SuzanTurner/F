
import requests
import dotenv
import os
import json
from user import ip, country, state, timestamp

dotenv.load_dotenv()
BASE_URL = os.getenv("BASE_URL")
# print(BASE_URL)

resp = requests.get(BASE_URL)
print("\n--- Home Route ---")
print(json.dumps(resp.json(), indent=2))

while True:
    inp = input("Press F to pay respect: ").strip()
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
