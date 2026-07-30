import requests


#TextGen API endpoint
API_URL = "http://127.0.0.1:5000/v1/chat/completions"
#Model currently loaded in TextGen
MODEL = "qwen2.5-7b-instruct-q4_k_m-00001-of-00002.gguf"


#Generate an AI response from the conversation history.
def generate_response(messages):
    payload = {
        "model": MODEL,
        "messages": messages
    }
    try:
        response = requests.post(API_URL, json = payload, timeout = 60)
        response.raise_for_status()

        data = response.json()
        return data["choices"][0]["message"]["content"]
    
    except requests.exceptions.RequestException as error:
        return f"API Error: {error}"