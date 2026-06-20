# 🎙️ Quantum AI Voice Calculator

A futuristic, voice-activated mathematical calculator featuring a sci-fi-inspired glassmorphism UI, natural language processing (NLP), and a highly secure Python backend. 

This project bridges the gap between natural human speech and complex mathematical computation. It allows users to speak conversational formulas, automatically filters out background noise and filler words, and delivers calculated audio feedback instantly.

---

## ✨ Key Features

* **Advanced Speech-to-Text Processing:** Utilizes the native browser Web Speech API to capture real-time voice input without requiring heavy external dependencies.
* **Natural Language NLP Parser:** A robust, custom-built JavaScript dictionary that translates conversational math (e.g., *"Calculate the square root of 16"*) into strict programmatic syntax (`sqrt(16)`).
* **Strict Whitelist Bouncer:** Actively ignores conversational filler words (*"what is"*, *"please calculate"*) while protecting vital math commands, ensuring the backend never crashes from bad grammar.
* **Secure Python Backend:** Calculations are routed to a local Flask server and safely evaluated using a restricted dictionary and a strict `__builtins__: None` sandbox rule, completely preventing arbitrary code injection.
* **Text-to-Speech (TTS) Output:** The application speaks the final calculated result back to the user via the SpeechSynthesis API.
* **Interactive Echo Mode:** A toggleable feature (`🔊 Echo: ON/OFF`) that repeats the user's recognized input before processing the calculation.
* **Manual Override:** The futuristic display panel doubles as an editable text field. Users can manually type or correct misheard inputs and press `Enter` to seamlessly recalculate.
* **Cyberpunk / Sci-Fi UI:** A sleek, single-page application with neon glowing states, animated UI components, and fully responsive design.

---

## 🧮 Supported Operations

The calculation engine supports a vast array of mathematical functions:
* **Basic Arithmetic:** Addition, Subtraction, Multiplication, Division.
* **Advanced Math:** Powers (`cubed`, `squared`, `to the power of`), Square Roots.
* **Trigonometry:** Sine, Cosine, Tangent (automatically converts spoken degrees to radians).
* **Rounding & Functions:** Ceiling, Floor, Absolute values, Factorials.
* **Logarithms:** Natural log (`log`), Base-10 log (`log 10`).
* **Constants:** Pi, Euler's number (`e`).

---

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **APIs:** Native Web Speech API (SpeechRecognition & SpeechSynthesis)
* **Backend:** Python 3, Flask framework

---

## 📂 Project Structure

```text
Voice-Calculator/
│
├── app.py                  # The Python Flask backend and secure evaluation engine
└── templates/
    └── index.html          # The frontend UI and Natural Language parsing logic