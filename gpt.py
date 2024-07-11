from keys import api_key
import requests
import json


def generate_response(user_message):
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_model = "gpt-3.5-turbo"

    body_message = {
        "model": id_model,
        "messages":[{"role": "user", "content": user_message}]
    }
    body_message = json.dumps(body_message)


    req = requests.post(link, headers=headers, data=body_message)
    response = req.json()
    message_response = response['choices'][0]['message']['content']

    return message_response

