# [Press F to Pay Respect API 💀](f-production-2a80.up.railway.app)

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

- `http://127.0.0.1:8000/` → *Press F to pay respect*  
- `http://127.0.0.1:8000/F` → *Respect sent to CRUD Lord*

### Example curl Commands

```bash
curl http://127.0.0.1:8000/                # "Press F to pay respect"
curl http://127.0.0.1:8000/F               # "Respect sent!"
curl http://127.0.0.1:8000/anything_else   # "bro press F"
```

## Author
👑 CRUD Lord — Yadhnika Wakde
