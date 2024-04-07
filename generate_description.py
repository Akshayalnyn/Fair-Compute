import base64
import requests


def generate_description(image_data):
    # Encode the image data in base64
    encoded_image = base64.b64encode(image_data).decode("utf-8")

    # API endpoint URL
    url = "http://8.12.5.48:11434/api/generate"

    # Your email and password for authentication
    email = "akshayalnyn@gmail.com"
    password = "akshu2001"

    # Payload data with an image encoded in base64
    payload = {
        "model": "llava:7b-v1.6-mistral-q5_K_M",
        "prompt": "Describe the dress in the image in detail.",
        "stream": False,
        "images": [encoded_image],
    }

    # Send POST request with authentication headers
    response = requests.post(url, json=payload, auth=(email, password))

    # Check response status
    if response.status_code == 200:
        # Return the response content
        return response.json()["response"]
    else:
        return f"Error accessing the API: {response.status_code} - {response.text}"
