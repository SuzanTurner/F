
import requests

while True:
    inp = input("Press F to pay respect: ").strip()
    if inp == 'F':
        resp = requests.get("https://f-production-2a80.up.railway.app/F")
        print("Respects Paid")
        break
    else:
        print("Bro, press F!")
