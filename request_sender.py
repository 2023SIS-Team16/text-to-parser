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

#Input as dict
def buffer_translate(input): 
    json_content = {
        'text': input['text'],
        'index': input['index'],
        'truncate': True,
    }

    print(f"Translating: {input['text']}")
    response = requests.get("http://127.0.0.1:5000/parse_text", json=json.dumps(json_content))
    print(f"Response: {response.json()['text']}")

    return {
        "result": response.json()['text'],
        "index": response.json()['index'],
    }

#Input as dict