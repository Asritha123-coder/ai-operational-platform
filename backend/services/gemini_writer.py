import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

BASE_URL = (
    "https://generativelanguage.googleapis.com/v1/models/"
    "gemini-2.5-flash:generateContent"
)

def generate_ai_report(analysis, root_causes, anomaly_msg, recommendations):
    prompt = f"""
You are an AI Ops engineer.

Generate an executive-level incident report based on the data below.

Issue Breakdown:
{analysis}

Root Cause Analysis:
{root_causes}

Anomaly Detection:
{anomaly_msg}

Recommended Actions:
{recommendations}

Write a concise, professional summary.
"""

    url = f"{BASE_URL}?key={API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        # Gemini response parsing
        return data["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        return f"AI summary unavailable: {str(e)}"
