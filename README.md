# SRE AI Log Analyzer

AI-powered support bundle analyzer for SRE teams.

## Features
- Support bundle extraction
- Log parsing
- Kubernetes analysis
- AI-based RCA (Llama3 via Ollama)

## Run

### Start API
uvicorn api.main:app --reload

### Start UI
streamlit run ui/app.py
