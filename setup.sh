#!/bin/bash

timestamp() {
  date +"[%Y-%m-%d %H:%M:%S]"
}

echo "$(timestamp) 🌟 setup.sh by Yadhnika 🚀"

# Check if venv exists
if [ -d "venv" ]; then
  echo "$(timestamp) 🐍 Virtual environment found, skipping creation."
else
  echo "$(timestamp) 🐍 Creating virtual environment..."
  python -m venv venv || { echo "❌ venv creation failed"; exit 1; }
fi

# Activate virtual environment cross-platform
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
  echo "$ ----- "
  echo "$ Windows User Detected"
  echo "$ ----- "
  echo "$(timestamp) 🔥 Activating virtual environment (Windows)..."
  source venv/Scripts/activate || { echo "❌ Activation failed"; exit 1; }
else
  echo "$(timestamp) 🔥 Activating virtual environment (Unix/Linux/macOS)..."
  source venv/bin/activate || { echo "❌ Activation failed"; exit 1; }
fi

# Download files only if missing
if [ ! -f "cli.py" ]; then
  echo "$(timestamp) 📥 Downloading cli.py..."
  curl -O https://raw.githubusercontent.com/SuzanTurner/F/main/cli.py || { echo "❌ cli.py download failed"; exit 1; }
else
  echo "$(timestamp) 📂 cli.py already exists, skipping download."
fi

if [ ! -f "requirements.txt" ]; then
  echo "$(timestamp) 📥 Downloading requirements.txt..."
  curl -O https://raw.githubusercontent.com/SuzanTurner/F/main/requirements.txt || { echo "❌ requirements.txt download failed"; exit 1; }
else
  echo "$(timestamp) 📂 requirements.txt already exists, skipping download."
fi

# Install dependencies only if needed
# (Simple approach: always run pip install, but you can improve with hash check)
echo "$(timestamp) 📦 Installing dependencies (will skip already installed)..."
pip install -r requirements.txt || { echo "❌ Dependency install failed"; exit 1; }

echo "$(timestamp) ▶️ Running cli.py..."
python cli.py || { echo "❌ cli.py execution failed"; exit 1; }

echo "$(timestamp) ✅ All done! ~ BackDev, Yadhnika"
