# Project Sentinel


## Project Sentinel er et avanceret beslutningsstøttesystem designet til at give sikkerhedspersonale en proaktiv evne til at identificere og mitigere potentielle trusler i realtid. Systemets kernefilosofi er ikke at erstatte menneskelig dømmekraft, men at forstærke den. Ved at analysere komplekse dataflows fra video, lyd og andre sensorer, giver Sentinel operatøren en dybere situationsforståelse, så de kan træffe mere informerede og effektive beslutninger.

Funktioner
Protokolbaseret AI-analyse: Specialiserede AI-protokoller (GABRIEL, RAFAEL, URIEL, AZRAEL, SERAPHIM, SANDALPHONE) arbejder sammen for at skabe et holistisk situationsbillede.

METATRON Prediktiv Syntese: Systemets kerne-AI, der samler data fra alle andre protokoller og genererer en samlet risikovurdering og prædiktive analyser.

Dynamisk Risikoanalyse: Interaktiv visualisering af trusselsscores baseret på simulerede hændelser.

Datapipeline Visualisering: Animeret flow af data gennem systemet.

Rollebaseret Adgangskontrol: Definerer klare adgangsniveauer og ansvar for Observatører, Feltoperatører og Administratorer.

Etiske Retningslinjer: Indlejret adfærdskodeks og nødprotokol (DEUS Override) for at sikre ansvarlig brug.

Interaktive Scenarier: Simulerede træningsscenarier for at demonstrere systemets funktionalitet i praksis.

Teknologier
Backend: Python 3 med Flask

Frontend: HTML5, Tailwind CSS, Vanilla JavaScript, Chart.js

Deployment/Automation: GitHub Actions (eksempel)

API Integration: Simuleret Gemini API-kald for METATRON

Opsætning og Kørsel
Følg disse trin for at få Project Sentinel til at køre lokalt på din maskine.

Forudsætninger
Python 3.8+

pip (Python pakkehåndtering)

En moderne webbrowser

Trin
Klon repository'et:

git clone https://github.com/din-bruger/project-sentinel.git
cd project-sentinel

Kør opsætningsscriptet:
Dette script vil opsætte Python-miljøet for backend'en, installere afhængigheder og starte både backend-serveren og åbne frontend'en i din webbrowser.

chmod +x scripts/setup_and_run.sh
./scripts/setup_and_run.sh

Backend'en vil køre på http://127.0.0.1:5000.

Frontend'en (frontend/index.html) vil åbne automatisk i din standard webbrowser.

Manuel Kørsel (alternativ):

Backend:

cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask run --port 5000

Backend'en vil nu køre på http://127.0.0.1:5000.

Frontend:
Åbn frontend/index.html direkte i din webbrowser.

Projektstruktur
project-sentinel/
├── backend/                  # Python Flask backend
│   ├── app.py                # Hovedapplikation og API-endpoints
│   └── requirements.txt      # Python afhængigheder
├── frontend/                 # HTML/CSS/JS frontend
│   └── index.html            # Enkeltsides webapplikation
├── .github/                  # GitHub Actions workflows
│   └── workflows/
│       └── main.yml          # CI/CD pipeline eksempel
├── scripts/
│   └── setup_and_run.sh      # Script til lokal opsætning og kørsel
├── README.md                 # Dette dokument
├── HOWTO.md                  # Detaljeret guide
├── WIKI.md                   # Wiki-indhold
└── QNA.md                    # Ofte stillede spørgsmål

Bidrag
Vi byder bidrag velkommen! Se venligst CONTRIBUTING.md (hvis den eksisterer) for retningslinjer.

Licens
Dette projekt er licenseret under MIT-licensen. Se LICENSE (hvis den eksisterer) for mere information.
# Project Sentinel

Project Sentinel is an advanced, interactive, browser-based security and analysis platform focused on real-time video, audio, and behavioral analytics. Built primarily with HTML, JavaScript, and modern libraries, the platform leverages facial recognition, emotion analysis, device clustering, GPS mapping, and predictive AI to create a persistent database of recognized individuals and actionable security insights.

## Features

- **Real-Time Facial Recognition:** Automatically detects, registers, and tracks new faces from live video streams, initially tagging them as "Ukjent" (Unknown).
- **Identity Management:** Operators can assign permanent names to recognized individuals, which are persisted in a cloud database (Firebase/Firestore).
- **Emotion & Behavior Analysis:** Utilizes `face-api.js` for emotion detection and provides real-time analytics on individual and group behavior.
- **AI Protocol Visualization:** Visualizes the operational status of multiple AI "protocols" (modules) for data integrity, emotion, group dynamics, environment, and predictive analytics.
- **Predictive Risk Analysis (METATRON):** Integrates with Gemini API to generate context-aware, predictive risk assessments based on the current scene.
- **Audio and Speech-to-Text:** Supports microphone selection and real-time transcription, associating speech with the most central detected individual.
- **GPS Mapping:** Displays device location on a map using Leaflet.js and simulates clustering analysis of nearby mobile devices.
- **Modern UI:** Built with Tailwind CSS and Lucide icons for a responsive and visually appealing interface.

## Technologies Used

- HTML, JavaScript (ES6+)
- [face-api.js](https://github.com/justadudewhohacks/face-api.js) for face detection and recognition
- [Tailwind CSS](https://tailwindcss.com/)
- [Leaflet.js](https://leafletjs.com/) for mapping
- [Lucide Icons](https://lucide.dev/)
- [Firebase](https://firebase.google.com/) (Authentication & Firestore)
- Google Gemini API for predictive analytics

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GizzZmo/Sentinel.git
   ```
2. **Open `index.html` in your web browser.**
3. **Configure Firebase:**  
   Provide your Firebase configuration either in the code or as a global variable.
4. **(Optional) Add your Gemini API key** in the system control panel for predictive analysis features.

## Usage

- Use the left panel for system status, protocol overviews, and device controls.
- The central area shows live video feeds, detection overlays, and group analysis.
- The right panel lists recognized individuals and provides analysis logs.
- Assign names to unknown individuals for permanent recognition.
- View predictive risk assessments powered by Gemini under the "METATRON" section.

## Screenshots

*(Add screenshots here of the UI in operation)*

## License

MIT

---
