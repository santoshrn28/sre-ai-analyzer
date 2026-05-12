from app.ai_engine import ask_llm

def analyze_logs(logs):
    combined = "\n".join(logs[:3])[:8000]

    prompt = f"""
You are an SRE expert.

Analyze logs and provide:
- summary
- root cause
- severity
- fix

Logs:
{combined}
"""
    return ask_llm(prompt)
