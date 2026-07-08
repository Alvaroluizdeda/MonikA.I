import requests

API_URL = "http://127.0.0.1:5000/v1/chat/completions"

MODEL = "qwen2.5-7b-instruct-q4_k_m-00001-of-00002.gguf"

def generate_response(user_input):
    payload = {
        "model": MODEL,
        "messages":[
            {   
                "role": "user",
                "content": user_input 
            }
        ]

    }

    response = requests.post(API_URL, json = payload)
    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"]


user_input = input("Usuário: ")
print(generate_response(user_input))