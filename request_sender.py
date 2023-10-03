import requests
import json

#Basic Request Translation
def request_translation(text):
    json_content = {
        'text': text,
        'index': 0,
        'truncate': False
    }

    print(f"Translating: {text}")
    response = requests.get("http://127.0.0.1:5000/parse_text", json=json.dumps(json_content))
    print(f"Response: {response.json()['text']}")
    return response.json()['text']