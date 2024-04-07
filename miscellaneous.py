import os
import requests
import base64

# API endpoint URL
url = "http://8.12.5.48:11434/api/generate"

# Your email and password for authentication
email = "akshayalnyn@gmail.com"
password = "akshu2001"


def generate_answer(question, image_path):
    # Read and encode the image in base64
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")

    # Payload data with an image encoded in base64
    payload = {
        "model": "llava:7b-v1.6-mistral-q5_K_M",
        "prompt": f"With the image as reference, answer the user's question: {question}",
        "stream": False,
        "images": [image_data],
    }

    # Send POST request with authentication headers
    response = requests.post(url, json=payload, auth=(email, password))

    # Check response status
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error accessing the API: {response.status_code} - {response.text}"
