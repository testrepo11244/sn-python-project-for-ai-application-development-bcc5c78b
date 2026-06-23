# Final Project: Emotion Detection with IBM Watson NLP

**Repository:** `oaqjp-final-project-emb-ai`

## Overview
This repository contains the complete source code for the IBM Skills Network capstone **Final Project**. The project demonstrates how to build an emotion detection application using IBM Watson Natural Language Processing (NLP) services, package it as a Python module, test it with unit tests, and deploy it as a Flask web service.

## Project Structure
```
oaqjp-final-project-emb-ai/
│
├─ emotion_detection/
│   ├─ __init__.py          # Makes the directory a package
│   └─ emotion_detection.py # Core logic for emotion analysis
│
├─ tests/
│   └─ test_emotion_detection.py # Unit tests
│
├─ server.py                # Flask web server for deployment
├─ requirements.txt         # Python dependencies
└─ README.md                # Project documentation (this file)
```

## Key Features
- **Watson NLP Integration:** Calls IBM Watson Natural Language Understanding to extract emotion scores.
- **Formatted Output:** Returns a JSON‑compatible dictionary with emotion percentages.
- **Error Handling:** Returns HTTP 400 responses for missing or empty input.
- **Package Validation:** `EmotionDetection` is a proper Python package.
- **Unit Testing:** Comprehensive tests using `unittest`.
- **Flask Deployment:** Simple web UI to submit text and view detected emotions.

## Getting Started
1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/oaqjp-final-project-emb-ai.git
   cd oaqjp-final-project-emb-ai
   ```

2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask server  
   ```bash
   python server.py
   ```

4. Execute unit tests  
   ```bash
   python -m unittest discover -s tests
   ```

## License
This project is licensed under the MIT License.

---  
*Prepared for the IBM Skills Network “Developing AI Applications with Python and Flask” course.*