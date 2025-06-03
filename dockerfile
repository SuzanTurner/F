FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y gcc python3-dev libpq-dev

RUN python -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

CMD ["/bin/bash", "-c", ". /opt/venv/bin/activate && exec uvicorn main:app --host 0.0.0.0 --port 8000"]
