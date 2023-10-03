import requests
import json

#Note: this is likely to truncate the final word of a sentence
def request_translation(text):
    json_content = {
        'text': text,
        'index': 0,
    }

    print(f"Translating: {text}")
    response = requests.get("http://127.0.0.1:5000/parse_text", json=json.dumps(json_content))
    print(f"Response: {response.json()}")
    return response.json()