# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import time
import random

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Mock data - In a real application, this would come from a database or external services
PROTOCOL_DATA = {
    "GABRIEL": {"title": "GABRIEL (Integritetsvakt)", "description": "Verifiserer integriteten og kvaliteten på innkommende data. Sikrer at ansiktsgjenkjenning opererer innenfor definerte kvalitetsparametere for å unngå feilidentifikasjon."},
    "RAFAEL": {"title": "RAFAEL (Bevegelsesanalyse)", "description": "Overvåker og analyserer bevegelsesmønstre. Identifiserer uvanlig flukt- eller forfølgelsesatferd, og synkroniserte bevegelser i grupper som kan indikere planlagt handling."},
    "URIEL": {"title": "URIEL (Miljøanalyse)", "description": "Oppdager avvik i det fysiske miljøet. Dette inkluderer deteksjon av potensielt farlige objekter (f.eks. forlatte gjenstander) og plutselige, høye lyder (f.eks. skrik, smell)."},
    "AZRAEL": {"title": "AZRAEL (Emosjonsanalyse)", "description": "Utfører dybdeanalyse av emosjonell tilstand basert på ansiktsuttrykk og (simulert) kroppsspråk. Identifiserer dominerende følelser som sinne, frykt og glede i en folkemengde."},
    "SERAPHIM": {"title": "SERAPHIM (Signalanalyse)", "description": "Simulerer triangulering av mobilenheter for å identifisere og spore gruppedannelse og klynger av mennesker, selv uten direkte visuell kontakt."},
    "SANDALPHONE": {"title": "SANDALPHONE (Sosial Dynamikk)", "description": "Evaluerer interaksjonen mellom individer og grupper. Analyserer sosial samhørighet, emosjonell smitte og dannelsen av 'ingrupper' og 'utgrupper'."},
    "METATRON": {"title": "METATRON (Prediktiv Syntese)", "description": "Systemets kjerne-AI. Samler data fra alle andre protokoller og bruker Gemini API til å generere en helhetlig risikovurdering og prediktive analyser om sannsynlige fremtidige hendelser."}
}

RISK_DATA = [
    {"protocol": "URIEL", "event": "Deteksjon av forlatt objekt", "score": 3},
    {"protocol": "URIEL", "event": "Høy lyd (skrik/smell)", "score": 2},
    {"protocol": "AZRAEL", "event": "Høy konsentrasjon av 'sinne' i gruppe", "score": 2},
    {"protocol": "AZRAEL", "event": "Høy konsentrasjon av 'frykt' (panikk)", "score": 3},
    {"protocol": "SANDALPHONE", "event": "Rask dannelse av stor, kohesiv gruppe", "score": 2},
    {"protocol": "SANDALPHONE", "event": "Høy negativ energi/smitte mellom grupper", "score": 5},
    {"protocol": "RAFAEL", "event": "Synkronisert, aggressiv bevegelse", "score": 4},
    {"protocol": "RAFAEL", "event": "Plutselig, kaotisk bevegelse (flukt)", "score": 3}
]

PIPELINE_DATA = [
    {"name": 'Sensor-input', "description": 'Kameraer/Mikrofoner'},
    {"name": 'GABRIEL', "description": 'Integritets-sjekk'},
    {"name": 'Parallell Analyse', "description": 'URIEL, RAFAEL, AZRAEL, SERAPHIM'},
    {"name": 'SANDALPHONE', "description": 'Sosial Syntese'},
    {"name": 'METATRON', "description": 'Prediktiv Analyse (Gemini API)'},
    {"name": 'Operatør-dashboard', "description": 'Analyse & Anbefaling'}
]

RULES_CONTENT = {
    "kodeks": """
        <h3 class="text-xl font-bold mb-4 text-slate-800">Kjerneverdier</h3>
        <ul class="space-y-4 list-disc list-inside text-slate-600">
            <li><strong>Bekreft før Handling:</strong> En AI-alarm er et utgangspunkt, ikke en ordre. Verifiser alltid funn.</li>
            <li><strong>Motstå Automatiseringsbias:</strong> Still alltid kritiske spørsmål til systemets konklusjoner. Ikke stol blindt på teknologien.</li>
            <li><strong>Respekter Personvern:</strong> Systemet skal kun brukes til legitime sikkerhetsformål innenfor lovens rammer.</li>
            <li><strong>Rapporter Avvik:</strong> Enhver feil, bias eller uetisk resultat skal umiddelbart rapporteres for systemforbedring.</li>
            <li><strong>Beskytt Data:</strong> All systemdata er sensitiv og skal behandles med høyeste grad av konfidensialitet.</li>
        </ul>""",
    "roller": """
        <div class="grid md:grid-cols-3 gap-6">
            <div class="bg-slate-50 p-6 rounded-lg">
                <h4 class="font-bold text-lg mb-2 text-slate-800">Nivå 1: Observatør</h4>
                <p class="text-sm text-slate-600"><strong>Tilgang:</strong> Kun lesetilgang til dashboard. Kan ikke iverksette tiltak. <strong>Formål:</strong> Situasjonsforståelse for støttepersonell.</p>
            </div>
            <div class="bg-slate-50 p-6 rounded-lg border-2 border-sky-500">
                <h4 class="font-bold text-lg mb-2 text-slate-800">Nivå 2: Feltoperatør</h4>
                <p class="text-sm text-slate-600"><strong>Tilgang:</strong> Full tilgang til sanntidsverktøy. Kan iverksette tiltak. <strong>Formål:</strong> Primærbruker under en operasjon.</p>
            </div>
            <div class="bg-slate-50 p-6 rounded-lg">
                <h4 class="font-bold text-lg mb-2 text-slate-800">Nivå 3: Administrator</h4>
                <p class="text-sm text-slate-600"><strong>Tilgang:</strong> Full systemtilgang, inkludert konfigurasjon og brukerstyring. <strong>Formål:</strong> Systemvedlikehold.</p>
            </div>
        </div>""",
    "nødprotokoll": """
        <div class="bg-red-50 border-l-4 border-red-500 text-red-700 p-6 rounded-r-lg">
            <h3 class="text-xl font-bold mb-4">DEUS Override</h3>
            <p class="text-red-800">I ekstraordinære situasjoner der en umiddelbar, overhengende trussel mot liv krever det, kan en operatør (Nivå 2+) aktivere <strong>DEUS Override</strong>.
            <ul class="mt-4 space-y-2 list-disc list-inside">
                <li><strong>Effekt:</strong> Deaktiverer midlertidig AI-anbefalinger og gir operatøren direkte kontroll.</li>
                <li><strong>Krav:</strong> Krever dobbel bekreftelse og skriftlig begrunnelse.</li>
                <li><strong>Logging:</strong> Utløser en høyprioritets-hendelse i systemets audit-logg for etterfølgende gjennomgang.</li>
            </ul>
            </p>
        </div>
        """
}

SCENARIOS = {
    "scenario1": [
        {"time": "12:01:05", "source": "SERAPHIM", "log": "Detekterer rask økning av enheter i Sone C."},
        {"time": "12:01:45", "source": "SANDALPHONE", "log": "Identifiserer to distinkte grupper (A, B). Intern energi nøytral."},
        {"time": "12:02:30", "source": "AZRAEL", "log": "Rapporterer kraftig økning i 'sinne' i Gruppe A."},
        {"time": "12:02:55", "source": "METATRON", "log": "PREDIKSJON: 93% sanns. for verbal konflikt innen 2 min. ANBEFALING: Etabler visuell tilstedeværelse. Sett trusselnivå til GUL."},
        {"time": "", "source": "OPERATØR", "log": "Anbefaling fulgt. Patrulje dirigert til Sone C."}
    ],
    "scenario2": [
        {"time": "22:50:10", "source": "RAFAEL", "log": "Flagger anomali: 3 individer beveger seg synkronisert og raskt."},
        {"time": "22:50:40", "source": "AZRAEL", "log": "Rapporterer atypisk lav emosjonell respons (nøytral) hos individene. Indikerer planlagt handling."},
        {"time": "22:51:05", "source": "METATRON", "log": "PREDIKSJON: Koordinert bevegelse indikerer høy intensjon. Potensial for innbrudd/hærverk. ANBEFALING: Følg individene live og varsle patrulje."},
        {"time": "", "source": "OPERATØR", "log": "Dedikerer monitor til å følge individer. Forhåndsvarsel sendt til patrulje."}
    ]
}

@app.route('/api/protocols', methods=['GET'])
def get_protocols():
    """Returns protocol data."""
    return jsonify(PROTOCOL_DATA)

@app.route('/api/risk_data', methods=['GET'])
def get_risk_data():
    """Returns risk event data."""
    return jsonify(RISK_DATA)

@app.route('/api/calculate_risk', methods=['POST'])
def calculate_risk():
    """
    Calculates total risk score based on selected events.
    Simulates METATRON's predictive synthesis and Gemini API call.
    """
    selected_risks = request.json.get('selectedRisks', {})
    total_score = sum(selected_risks.values())

    # Simulate Gemini API call for a comprehensive risk assessment
    # In a real scenario, this would involve a call to an actual LLM API
    # For this mock, we'll just generate a simple assessment based on the score
    risk_assessment = ""
    if total_score == 0:
        risk_assessment = "Situasjonen er rolig og stabil. Ingen umiddelbare trusler identifisert."
    elif total_score <= 4:
        risk_assessment = "Lav til moderat risiko. Mindre avvik er observert, men ingen umiddelbar fare. Fortsett overvåkning."
    elif total_score <= 9:
        risk_assessment = "Moderat til høy risiko. Betydelige avvik er detektert. Anbefales økt årvåkenhet og forberedelse på mulige tiltak."
    else:
        risk_assessment = "Kritisk risiko! Umiddelbar trussel er identifisert. Handling er påkrevd for å de-eskalere situasjonen."

    # Simulate some processing time
    time.sleep(0.5)

    return jsonify({
        "totalScore": total_score,
        "riskAssessment": risk_assessment
    })

@app.route('/api/pipeline_data', methods=['GET'])
def get_pipeline_data():
    """Returns pipeline visualization data."""
    return jsonify(PIPELINE_DATA)

@app.route('/api/rules_content', methods=['GET'])
def get_rules_content():
    """Returns content for the rules and guidelines section."""
    return jsonify(RULES_CONTENT)

@app.route('/api/scenarios', methods=['GET'])
def get_scenarios():
    """Returns scenario data for training simulations."""
    return jsonify(SCENARIOS)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
