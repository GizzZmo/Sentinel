# HOWTO: Project Sentinel - Detaljeret Guide

Denne guide giver en mere dybdegående forklaring på, hvordan man opsætter, kører og forstår
Project Sentinel-systemet.

## 1. Forstå Arkitekturen

Project Sentinel er bygget som en simpel klient-server-applikation:

### Frontend (frontend/index.html)

Dette er en statisk HTML-fil, der indeholder al brugergrænseflade (HTML), styling (Tailwind CSS)
og interaktiv logik (Vanilla JavaScript). Den kalder backend'en for at hente dynamiske data.

### Backend (backend/app.py)

Dette er en Python Flask-applikation, der fungerer som en RESTful API. Den leverer data til
frontend'en og udfører den simulerede "METATRON" risikoanalyse.

Kommunikationen mellem frontend og backend sker via HTTP-anmodninger (GET og POST) over et lokalt
netværk (eller internettet, hvis implementeret).

## 2. Opsætning af Udviklingsmiljøet

Sørg for, at du har de nødvendige værktøjer installeret:

- **Python 3:** Download og installer fra python.org.
- **Git:** Download og installer fra git-scm.com.

### 2.1 Kloning af Repository

Åbn din terminal eller kommandoprompt og kør:

```bash
git clone https://github.com/din-bruger/project-sentinel.git
cd project-sentinel
```

Erstat `https://github.com/din-bruger/project-sentinel.git` med den faktiske URL til dit repository.

### 2.2 Opsætning af Backend

Naviger til backend-mappen:

```bash
cd backend
```

Opret et virtuelt miljø: Det anbefales stærkt at bruge virtuelle miljøer for at isolere projektets
afhængigheder.

```bash
python3 -m venv venv
```

Aktiver det virtuelle miljø:

**macOS/Linux:**

```bash
source venv/bin/activate
```

**Windows (Cmd):**

```cmd
.\venv\Scripts\activate.bat
```

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

Installer afhængigheder:

```bash
pip install -r requirements.txt
```

Dette vil installere Flask og Flask-CORS.

## 3. Kørsel af Systemet

### 3.1 Start Backend-serveren

Mens du stadig er i backend-mappen med det virtuelle miljø aktiveret:

```bash
export FLASK_APP=app.py
flask run --port 5000
```

Du skulle nu se output, der indikerer, at Flask-serveren kører på <http://127.0.0.1:5000>.
Hold denne terminal åben.

### 3.2 Start Frontend-applikationen

Åbn en ny terminal eller kommandoprompt.
Naviger tilbage til projektets rodmappe:

```bash
cd .. # Hvis du er i 'backend'-mappen
```

Åbn index.html:
Du kan simpelthen åbne filen i din webbrowser.

**macOS:**

```bash
open frontend/index.html
```

**Linux:**

```bash
xdg-open frontend/index.html
```

**Windows:**

```cmd
start frontend/index.html
```

Alternativt kan du navigere til `file:///sti/til/dit/projekt/frontend/index.html` i din browser.

Systemet er nu fuldt operationelt. Frontend'en vil automatisk kommunikere med backend'en, der
kører på <http://127.0.0.1:5000>.

## 4. Forstå Backend API'et

Backend'en (app.py) udstiller følgende API-endpoints:

- **GET /api/protocols:** Henter data om de forskellige AI-protokoller.
- **GET /api/risk_data:** Henter data om de simulerede risikohændelser og deres pointværdier.
- **POST /api/calculate_risk:** Modtager en JSON-payload med valgte risici og returnerer den
  samlede trusselsscore og en simuleret risikovurdering fra METATRON.
- **GET /api/pipeline_data:** Henter data for visualisering af datapipelinen.
- **GET /api/rules_content:** Henter indhold til etiske retningslinjer, roller og nødprotokol.
- **GET /api/scenarios:** Henter data for træningsscenarierne.

## 5. Fejlfinding

### "Could not connect to backend" / CORS-fejl

Sørg for, at Flask-backend'en kører på <http://127.0.0.1:5000>. Tjek terminalen, hvor du
startede Flask.

Kontroller, at `CORS(app)` er aktiveret i app.py.

### Python-afhængighedsfejl

Sørg for, at du har aktiveret det virtuelle miljø (`source venv/bin/activate`) før du kører
`pip install -r requirements.txt` og `flask run`.

### Frontend-interaktioner virker ikke

Åbn browserens udviklerværktøjer (F12) og tjek konsollen for JavaScript-fejl.

Sørg for, at API_BASE_URL i index.html's JavaScript stemmer overens med din Flask-backend's URL.

## 6. Stop Systemet

For at stoppe Flask-backend'en skal du gå til den terminal, hvor den kører, og trykke Ctrl+C.
Hvis du startede den med nohup, skal du finde process-ID'en (PID) og dræbe den:

```bash
# Find PID'en for Flask-processen
lsof -i :5000
# Eller
ps aux | grep flask

# Dræb processen (erstat <PID> med det faktiske nummer)
kill <PID>
```

Luk derefter din webbrowser.
