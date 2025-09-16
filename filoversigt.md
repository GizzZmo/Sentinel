# Project Sentinel Filoversigt

Dette er en oversigt over filerne og mappestrukturen for Project Sentinel-systemet.

```text
project-sentinel/
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   └── index.html
├── .github/
│   └── workflows/
│       └── main.yml  (Eksempel på GitHub Actions workflow)
├── scripts/
│   └── setup_and_run.sh
├── README.md
├── HOWTO.md
├── WIKI.md
└── QNA.md
```

## Filbeskrivelser

**backend/app.py:** Python Flask-applikation, der fungerer som systemets backend. Den håndterer
API-kald, simulerer METATRON's logik og leverer data til frontend.

**backend/requirements.txt:** Liste over Python-afhængigheder for backend'en.

**frontend/index.html:** Den enkeltsides webapplikation (SPA) med HTML, Tailwind CSS og
JavaScript, der interagerer med backend'en.

**.github/workflows/main.yml:** Et eksempel på en GitHub Actions-workflow, der kan bruges til
CI/CD (kontinuerlig integration/kontinuerlig levering).

**scripts/setup_and_run.sh:** Et shell-script til at opsætte og køre både backend og frontend
lokalt.

**README.md:** Den primære dokumentation for projektet, der giver en hurtig oversigt og
opsætningsinstruktioner.

**HOWTO.md:** En mere detaljeret guide til at køre og forstå projektet.

**WIKI.md:** Konceptuelt indhold til et GitHub Wiki.

**QNA.md:** Ofte stillede spørgsmål og svar.
