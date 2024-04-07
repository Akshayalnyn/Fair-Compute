import os
import requests
import base64
import streamlit as st


def generate_insta_caption(image_path):
    # API endpoint URL
    url = st.secrets["llava_url"]

    # Your email and password for authentication
    email = st.secrets["email"]
    password = st.secrets["pwd"]

    # Read and encode the image in base64
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")

    # Payload data with an image encoded in base64
    payload = {
        "model": "llava:7b-v1.6-mistral-q5_K_M",
        "prompt": "Write an Instagram caption for me for the dress in the image.",
        "stream": False,
        "images": [image_data],
    }

    # Send POST request with authentication headers
    response = requests.post(url, json=payload, auth=(email, password))

    # Check response status
    if response.status_code == 200:
        # Return the generated caption
        return response.json()["response"]
    else:
        print(f"Error accessing the API: {response.status_code} - {response.text}")
        return None
