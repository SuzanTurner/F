# Run this in your terminal
```
iwr https://raw.githubusercontent.com/SuzanTurner/F/main/cli.py -OutFile temp_cli.py; python temp_cli.py; Remove-Item temp_cli.py
```

# Or this in bash
```
curl -O https://raw.githubusercontent.com/SuzanTurner/F/main/setup.sh && bash setup.sh
```

# 🪦 Press F to Pay Respect - FastAPI App

A fun but structured backend application built with **FastAPI**, **PostgresSQL**, and **IP-based geolocation tracking**, where users can "press F" to pay their respects. Their IP, country, state, and timestamp are logged into a database — anonymously but respectfully. 🫡

## 📜 Features

- `/` → Welcome route with basic instructions and info.
- `/f` → Tells users to press **F**.
- `/F` → Accepts user data and logs it into the database.
- `/log` → Displays all users who pressed F with timestamp & location.
- `/anything` → Handles all other nonsense with a friendly *"bro press F"*.

## 🧠 Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **IP Geolocation API**: [ipstack.com](https://ipstack.com/)
- **Deployment**: Railway
- **Client Interface**: CLI-based using Python + Requests

## 🧾 How It Works

1. A user runs the CLI script.
2. On pressing `F`, their:
   - IP Address
   - Country
   - State
   - Timestamp  
   ...are fetched using **ipstack** API.
3. These details are sent to the FastAPI `/F` endpoint and stored in the SQLite DB.

## 📂 Project Structure

```
project/
│
├── main.py 
├── user.py 
├── cli.py 
├── models.py 
├── schemas.py 
├── db.py 
├── .env 
├── requirements.txt 
└── README.md 
```




## Sample Response
```
User with IP Address 43.247.156.164 from India Uttar Pradesh sent respect at 2025-06-02 21:15:00
```

## 🚀 Running Locally
1. Clone this repo
```
git clone https://github.com/SuzanTurner/F.git
```
2. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
3. Install dependencies
```
pip install -r requirements.txt
```

4. Run the fastapi app:
```
uvicorn main:app --reload
```

5. Run the CLI script
```
python cli.py
```

## Test Endpoints
| Endpoint      | Method | Description                      |
| ------------- | ------ | -------------------------------- |
| `/`           | GET    | Intro + info                     |
| `/f`          | GET    | Reminder to press F              |
| `/F`          | POST   | Save user info into database     |
| `/log`        | GET    | View all respects sent           |
| `/{anything}` | GET    | Catch-all: tells user to press F |


## 🤝 Contributions
Pull requests are welcome, but respectfully

---

### Author - Yadhnika Wakde


