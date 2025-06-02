# Run this in your terminal
```
iwr https://raw.githubusercontent.com/SuzanTurner/F/main/cli.py -OutFile temp_cli.py; python temp_cli.py; Remove-Item temp_cli.py
```

## What’s This?
Press F to pay respect

## Endpoints

| Endpoint | Method | Description                              |
| -------- | ------ | -------------------------------------  |
| `/`      | GET    | Returns a message: *Press F to pay respect* |
| `/F`     | GET    | Returns the official *Respect sent*  |


## How to Run Locally
1. Clone the repo
2. Install dependencies:
```
pip install -r requirements.txt
```
4. Run the app:
```
uvicorn main:app --reload
```
5. Open your browser or terminal and try:

- 'https://f-production-2a80.up.railway.app' → *Press F to pay respect*  
- 'https://f-production-2a80.up.railway.app/F' → *Respect sent to CRUD Lord*

### Example curl Commands

```bash
curl https://f-production-2a80.up.railway.app                # "Press F to pay respect"
curl https://f-production-2a80.up.railway.app/F             # "Respect sent!"
curl https://f-production-2a80.up.railway.app/anything_else   # "bro press F"
```

## Author
👑 CRUD Lord — Yadhnika Wakde
