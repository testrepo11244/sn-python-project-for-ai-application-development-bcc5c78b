# oaqjp-final-project-emb-ai

## Project Overview
This repository contains the final capstone project for the IBM Skills Network course **Developing AI Applications with Python and Flask**. The project implements an **Emotion Detection** web application using IBM Watson Natural Language Processing (NLP) services, packaged as a Flask API and deployed locally for testing.

### Key Features
- **Emotion detection** using Watson NLP library.
- Properly formatted JSON output with detected emotions and confidence scores.
- Comprehensive unit tests (`test_emotion_detection.py`) ensuring correct functionality.
- Flask web server (`server.py`) exposing a REST endpoint for client interaction.
- Error handling for invalid or empty input (HTTP 400 responses).
- Static code analysis integration with `pylint` achieving a perfect score.

### Repository Structure
```
oaqjp-final-project-emb-ai/
│
├── emotion_detection.py          # Core emotion detection logic
├── EmotionDetection/               # Python package
│   ├── __init__.py                # Package initializer
│   └── ...                         # Additional modules (if any)
├── server.py                       # Flask application exposing the API
├── test_emotion_detection.py       # Unit tests for the emotion detector
├── requirements.txt                # Project dependencies
├── README.md                       # Project documentation (this file)
└── screenshots/
    ├── 6b_deployment_test.png
    └── 7c_error_handling_interface.png
```

### How to Run the Application
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/oaqjp-final-project-emb-ai.git
   cd oaqjp-final-project-emb-ai
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set up IBM Watson credentials**
   - Export your Watson API key and URL as environment variables:
     ```bash
     export WATSON_API_KEY=your_api_key
     export WATSON_URL=your_service_url
     ```

4. **Run the Flask server**
   ```bash
   python server.py
   ```

5. **Test the endpoint**
   ```bash
   curl -X POST http://127.0.0.1:5000/emotion-detection \
        -H "Content-Type: application/json" \
        -d '{"text": "I am thrilled about the new project!"}'
   ```

### License
This project is licensed under the MIT License.

--- 

*Prepared for the IBM Skills Network capstone submission.*