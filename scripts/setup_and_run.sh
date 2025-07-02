#!/bin/bash

# scripts/setup_and_run.sh
# Dette script opsætter og starter Project Sentinel-backend'en og frontend'en lokalt.

echo "Starter opsætning af Project Sentinel..."

# --- Backend Opsætning og Start ---
echo "Opsætter Python backend..."
# Opretter og aktiverer et virtuelt miljø
python3 -m venv backend/venv
source backend/venv/bin/activate

# Installerer Python-afhængigheder
pip install -r backend/requirements.txt

echo "Starter Flask backend..."
# Eksporterer Flask applikationen og starter den i baggrunden
export FLASK_APP=backend/app.py
nohup flask run --port 5000 > backend/flask_output.log 2>&1 &
BACKEND_PID=$!
echo "Flask backend kører på PID: $BACKEND_PID"
echo "Backend output logges til backend/flask_output.log"

# Deaktiverer det virtuelle miljø
deactivate

# --- Frontend Start ---
echo "Åbner frontend i standard webbrowser..."
# Åbner index.html direkte i webbrowseren.
# Bemærk: For mere komplekse frontend-projekter med build-processer
# ville du her starte en lokal webserver (f.eks. 'python3 -m http.server 8000'
# eller en Node.js-baseret server) og derefter åbne den URL.
xdg-open frontend/index.html || open frontend/index.html || start frontend/index.html

echo "Project Sentinel er startet."
echo "For at stoppe backend'en, kør 'kill $BACKEND_PID' i din terminal."
echo "Du kan også finde PID'en med 'lsof -i :5000' eller 'ps aux | grep flask'."

