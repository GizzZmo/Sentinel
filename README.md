Here’s a README.md and About section based on the code in your index.html file for Project Sentinel:

---

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
