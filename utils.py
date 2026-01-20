import json
import os
from datetime import datetime

def load_json(file_path):
    """Load JSON data safely"""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return {}

def save_json(data, file_path):
    """Save JSON data"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def log_call_data(transcript, sentiment, recommendations, timestamp):
    """Log call data for post-call analysis"""
    call_data = {
        "timestamp": timestamp,
        "transcript": transcript,
        "sentiment": sentiment,
        "recommendations": recommendations
    }
    calls = load_json("data/sales_calls.json")
    calls.append(call_data)
    save_json(calls, "data/sales_calls.json")
