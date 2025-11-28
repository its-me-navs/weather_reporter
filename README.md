# 🌤️ Weather → Gemini Example

Small Python example that fetches current weather (via WeatherAPI) and sends the JSON to a Gemini model to generate a short report.

Files
- [gemini_api_code.py](gemini_api_code.py)
- [weather_api.py](weather_api.py)
- [__pycache__](__pycache__/)

Key symbol
- The weather helper used is [`weather_api.weather`](weather_api.py)

Quick overview
- `weather_api.weather()` requests current weather for Bangalore and returns the JSON as a string.
- `gemini_api_code.py` prints that JSON and calls a Gemini client to generate a ~100-word weather report.

Requirements
- Python 3.8+
- pip packages:
  - requests
  - google-genai

Setup
1. Create and activate a virtualenv:
```bash
python -m venv .venv
source .venv/bin/activate    # macOS / Linux
.venv\Scripts\activate       # Windows
```

2. Install dependencies:
```bash
pip install requests google-genai
```

Configuration (IMPORTANT)
- Replace hard-coded API keys in the source files. Current locations:
  - [weather_api.py](weather_api.py) contains the WeatherAPI URL with `key=<your_api_key_here>`.
  - [gemini_api_code.py](gemini_api_code.py) currently sets the client with an inline API key.
- Recommended: use environment variables, e.g. `WEATHERAPI_KEY` and `GENAI_API_KEY`, and read them in code.

Run
- Print weather JSON:
```bash
python weather_api.py
```
- Run the Gemini example:
```bash
python gemini_api_code.py
```

Notes & suggested fixes
- Fix the duplicate assignment in [weather_api.py](weather_api.py): `response = response = ...` should be `response = requests.get(...)`.
- Read API keys from env vars instead of embedding them.
- Add error handling and timeouts to `requests.get`, and validate `response.status_code` before calling `.json()`.

Security 🔒
- Do NOT commit API keys. Add secrets to environment variables and include them in `.gitignore`.

Contributing
- Improvements welcome: better error handling, CLI/config support, and tests.

License
- Add a LICENSE file as appropriate.