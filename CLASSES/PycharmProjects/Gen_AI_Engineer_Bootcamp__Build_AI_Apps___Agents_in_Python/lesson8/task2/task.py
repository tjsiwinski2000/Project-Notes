import requests

API_URL = "http://localhost:5002"
url = f"{API_URL}/chat"
history = []

while True:
    user_input = input("You: ")

    # TODO: append {'role': 'user', 'content': user_input} to history; POST to url with json={'messages': history} and store in response; take response.json()['message'] as assistant_message, append it to history, and print assistant_message['content']
