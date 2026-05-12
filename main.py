from fastapi import FastAPI, UploadFile
import shutil

from app.extractor import extract_bundle
from app.log_loader import load_logs
from app.analyzer import analyze_logs

app = FastAPI()

@app.get("/")
def home():
    return {"status": "SRE Analyzer Running"}

@app.post("/analyze/")
async def analyze(file: UploadFile):
    path = f"data/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    folder = extract_bundle(path)
    logs = load_logs(folder)

    result = analyze_logs(logs)

    return {"analysis": result}
