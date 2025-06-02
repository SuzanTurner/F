
import requests
import dotenv
import os
import json

dotenv.load_dotenv()
BASE_URL = os.getenv("BASE_URL")
print(BASE_URL)

resp = requests.get(BASE_URL)
print("\n--- Home Route ---")
print(json.dumps(resp.json(), indent=2))

while True:
    inp = input("Press F to pay respect: ").strip()
    if inp == 'F':
        resp = requests.get(f"{BASE_URL}/F")
        print(json.dumps(resp.json(), indent=2))
        break
    else:
        resp = requests.get(f"{BASE_URL}/{inp}")
        print(json.dumps(resp.json(), indent=2))
