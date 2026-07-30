import json
from memory_extractor import extract_memories
from api_client import generate_response

# test_messages = [
#     "My name is Álvaro and i have 20 years.Today,i'm sad, my cat's name is Tonico, now i'm playing videogames."
#  ]

# for message in test_messages:
#     print("="*40)
#     print(f"Input: {message}")

#     memories = extract_memories(message)
#     print(f"Output: {memories}")
# exit()

#Maximum number of messages stored in the conversation history(includes: System, user and assistant).
MAX_MESSAGES = 80

#Loads for the user memory from the JSON file.
def load_memory():
    with open("MonikA.I/data/memory.json", "r", encoding = "utf-8") as file:
        memory = json.load(file)

    return memory

#Adds a new memory if it does not already exist.
def add_memory(memory, fact):
    if fact.lower() not in [f.lower() for f in memory["facts"]]:
       memory["facts"].append(fact)

# Saves the current user memory to the JSON file.
def save_memory(memory):
    with open("MonikA.I/data/memory.json", "w", encoding = "utf-8") as file:
        json.dump(memory, file, ensure_ascii = False, indent = 4)

##test

memory = load_memory()
test_messages = ["Eu gosto de programar", "Eu estudo ciências da computação", "Eu gosto de gatos"]
for message in test_messages:
    facts = extract_memories(message)

    for fact in facts:
        add_memory(memory,fact)

save_memory(memory)
print(load_memory())
exit()


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

    #Loop to clear history.
    while len(messages) > MAX_MESSAGES + 1:
        messages.pop(1)


