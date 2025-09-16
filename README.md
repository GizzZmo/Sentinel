# Project Sentinel

Project Sentinel is an advanced, interactive security and threat analysis platform designed to provide security
personnel with proactive capabilities for identifying and mitigating potential threats in real-time. The system's
core philosophy is not to replace human judgment, but to enhance it. By analyzing complex data flows from video,
audio, and other sensors, Sentinel provides operators with deeper situational awareness to make more informed and
effective decisions.

## 🎯 Overview

This platform combines real-time facial recognition, emotion analysis, device clustering, GPS mapping, and
predictive AI to create a comprehensive security analytics solution. It operates as a browser-based application
with a Python Flask backend providing simulated AI protocol data and risk assessments.

## 🚀 Key Features

### AI Protocol System

- **GABRIEL (Integrity Guard):** Verifies data integrity and quality of incoming feeds
- **RAFAEL (Movement Analysis):** Monitors and analyzes movement patterns for unusual behavior
- **URIEL (Environmental Analysis):** Detects environmental anomalies and potential threats
- **AZRAEL (Emotion Analysis):** Performs deep emotion analysis based on facial expressions
- **SERAPHIM (Signal Analysis):** Simulates mobile device triangulation for group detection
- **SANDALPHONE (Social Dynamics):** Evaluates interactions between individuals and groups
- **METATRON (Predictive Synthesis):** Core AI that generates comprehensive risk assessments

### Real-Time Capabilities

- **Facial Recognition:** Automatically detects and tracks faces from live video streams
- **Identity Management:** Persistent database of recognized individuals with naming capabilities
- **Behavior Analytics:** Real-time analysis of individual and group behavior patterns
- **Risk Assessment:** Context-aware predictive risk analysis using AI protocols
- **Audio Processing:** Speech-to-text with speaker association
- **GPS Mapping:** Device location visualization and clustering analysis

### User Interface

- **Modern Design:** Built with Tailwind CSS and Lucide icons
- **Role-Based Access:** Three-tier access system (Observer, Field Operator, Administrator)
- **Real-Time Dashboards:** Live visualization of all AI protocols and risk metrics
- **Interactive Controls:** System configuration and emergency override capabilities

## 🛠️ Technology Stack

### Backend

- **Python 3.8+** with Flask framework
- **Flask-CORS** for cross-origin resource sharing
- RESTful API architecture

### Frontend

- **HTML5** with modern JavaScript (ES6+)
- **[Tailwind CSS](https://tailwindcss.com/)** for styling
- **[face-api.js](https://github.com/justadudewhohacks/face-api.js)** for facial recognition
- **[Leaflet.js](https://leafletjs.com/)** for mapping
- **[Lucide Icons](https://lucide.dev/)** for UI icons

### Optional Integrations

- **Firebase/Firestore** for data persistence
- **Google Gemini API** for enhanced AI predictions

## 📦 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Quick Start

1. **Clone the repository:**

   ```bash
   git clone https://github.com/GizzZmo/Sentinel.git
   cd Sentinel
   ```

2. **Run the setup script:**

   ```bash
   chmod +x scripts/setup_and_run.sh
   ./scripts/setup_and_run.sh
   ```

   This script will:
   - Set up the Python virtual environment
   - Install backend dependencies
   - Start the Flask server on `http://127.0.0.1:5000`
   - Open the frontend in your default browser

### Manual Setup

If you prefer manual setup:

1. **Backend setup:**

   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   export FLASK_APP=app.py
   flask run --port 5000
   ```

2. **Frontend setup:**
   Simply open `index.html` in your web browser, or serve it through a local web server.

## 📁 Project Structure

```text
Sentinel/
├── backend/                    # Python Flask backend
│   ├── app.py                 # Main application and API endpoints
│   └── requirements.txt       # Python dependencies
├── scripts/                   # Automation scripts
│   └── setup_and_run.sh      # Setup and deployment script
├── .github/                   # GitHub Actions workflows
│   └── workflows/
│       └── main.yml          # CI/CD pipeline
├── index.html                 # Main frontend application
├── infografikk.html          # System architecture visualization
├── README.md                 # This documentation
├── HowTo.md                  # Detailed setup guide
├── WIKI.md                   # System philosophy and concepts
├── Operatørmanual.md         # Operator manual (Norwegian)
├── example.md                # Example usage scenarios
├── example_minimal.md        # Minimal setup example
├── filoversigt.md           # File overview (Danish)
└── MARKDOWN_LINT.md         # Markdown linting guidelines
```

## 🎮 Usage

### Getting Started

1. Start the backend server using the setup script or manual installation
2. Open the frontend in your web browser
3. The system will load with simulated data and AI protocols active

### Main Interface

- **Left Panel:** System status, protocol overviews, and device controls
- **Central Area:** Live video feeds, detection overlays, and group analysis
- **Right Panel:** Recognized individuals list and analysis logs

### Key Operations

- **Monitor Protocols:** Track the status of all AI analysis modules
- **View Risk Assessments:** Real-time threat level analysis and predictions
- **Manage Identities:** Name and track recognized individuals
- **Generate Reports:** Export analysis data and system logs

### Security Features

- **Role-based access control** with three security levels
- **Emergency override (DEUS Protocol)** for critical situations
- **Audit logging** of all system actions and decisions
- **Ethical guidelines** embedded in system operation

## 📊 API Documentation

The backend provides several REST endpoints:

- `GET /api/protocols` - Get all AI protocol information
- `GET /api/risk_data` - Get current risk event data
- `POST /api/calculate_risk` - Calculate comprehensive risk assessment
- `GET /api/pipeline_data` - Get data processing pipeline status
- `GET /api/scenarios` - Get training scenario data

## 🤝 Contributing

Contributions are welcome! Please read our contributing guidelines and ensure your code follows the project standards.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- Check the [HowTo.md](HowTo.md) for detailed setup instructions
- Read the [WIKI.md](WIKI.md) for system concepts and philosophy
- Review the [Operator Manual](Operatørmanual.md) for operational procedures

## ⚠️ Disclaimer

This is a demonstration platform designed for educational and development purposes. It simulates security analysis
capabilities and should not be used for actual security operations without proper validation, testing, and
compliance with applicable laws and regulations.

---

**Project Sentinel** - Enhancing human judgment through intelligent analysis
