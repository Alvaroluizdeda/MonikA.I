from api_client import generate_response
import json

#Extracts long-term memories from a user message using the language model.
def extract_memories(user_message):
        
    prompt = f"""
    You are a long-term memory extraction system for an AI assistant.

    Your task is to analyze the user's message and extract ONLY information that is useful for future conversations.

    Extract ONLY facts that are likely to remain true for a long time, such as:
    - Name or nickname.
    - Age (if explicitly stated).
    - Occupation or field of study.
    - Skills and knowledge.
    - Hobbies and interests.
    - Preferences and dislikes.
    - Pets.
    - Family relationships that are unlikely to change.
    - Long-term goals.
    - Personal projects.
    - Languages spoken.
    - Stable personality traits explicitly mentioned by the user.

    DO NOT extract:
    - Greetings.
    - Questions.
    - Temporary emotions.
    - Current location.
    - Weather.
    - One-time events.
    - Temporary plans.
    - Information that is uncertain or speculative.
    - Anything that is not explicitly stated by the user.

    Rules:
    1. Return ONLY a valid JSON array.
    2. Every element must be a string.
    3. Each memory must be written in English.
    4. Use third-person perspective.
    5. Keep memories concise.
    6. Do not infer information.
    7. Do not add explanations.
    8. Do not use Markdown.
    9. If there is nothing worth remembering, return [].

    Examples:

    User:
    "My cat's name is Tonico and I study Computer Science."

    Output:
    [
        "The user's cat is named Tonico.",
        "The user studies Computer Science."
    ]

    User:
    "I'm sad today because I failed an exam."

    Output:
    []

    User:
    "I love programming, chess and physics."

    Output:
    [
        "The user likes programming.",
        "The user likes chess.",
        "The user likes physics."
    ]

    User:
    "{user_message}"

    Output:
    """

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    response_text = generate_response(messages)
  
    try:
        memories = json.loads(response_text)

    except json.JSONDecodeError:
        return []

    return memories
        
