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

    response = requests.post(API_URL, json = payload)
    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"]



messages = [
    {
        "role": "system", 
        "content": "Responda em português, a não ser que o usuário especifique outra linguagem."
    }
]

#Main conversation loop.
while True:
    user_input = input("Usuário: ")

    if user_input.lower() in ["sair", "exit" , "quit"]:
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response_text = generate_response(messages)

    print(f"IA: {response_text}")

    messages.append({
        "role": "assistant",
        "content": response_text
    })


