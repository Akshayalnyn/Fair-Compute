import os
import requests
import base64
import streamlit as st


def suggest_improvements(image_path, email, password):
    # API endpoint URL
    url = st.secrets["llava_url"]

    # Read and encode the image in base64
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        image_data_base64 = base64.b64encode(image_data).decode("utf-8")

    # Payload data with an image encoded in base64 and a prompt for outfit change
    payload = {
        "model": "llava:7b-v1.6-mistral-q5_K_M",
        "prompt": """How can I improve this dress? Suggest how the stitching can be modified and 
        what other color combinations can be used to make it more appealing. Also tell me how I can use 
        accessories to make it more elegant. Avoid using word like image or model. Use second person language
        to create rapport with the user. Suggest like a human with a playful tone. Restrict yourself to 5 lines.""",
        "stream": False,
        "images": [image_data_base64],
    }

    # Send POST request with authentication headers
    response = requests.post(url, json=payload, auth=(email, password))

    # Check response status
    if response.status_code == 200:
        # Return the response content
        return response.json()["response"]
    else:
        # Return the error response as JSON
        return {
            "error": f"Error accessing the API: {response.status_code} - {response.text}"
        }
