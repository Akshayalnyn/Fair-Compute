import requests
import base64
import streamlit as st

def get_occasion_suggestions(image_data):
    # API endpoint URL
    url = st.secrets["llava_url"]

    # Your email and password for authentication
    email = st.secrets["email"]
    password = st.secrets["pwd"]

    # Payload data with an image encoded in base64 and a prompt for occasion suggestions
    payload = {
        "model": "llava:7b-v1.6-mistral-q5_K_M",
        "prompt": """Which occasion does this outfit suit? Avoid using word like image or model. 
                    Use second person language to create rapport with the user. Suggest like a human with a playful tone.""",
        "stream": False,
        "images": [image_data],
    }

    # Send POST request with authentication headers
    response = requests.post(url, json=payload, auth=(email, password))

    # Check response status
    if response.status_code == 200:
        # Return the response content
        return response.json()["response"]
    else:
        return f"Error accessing the API: {response.status_code} - {response.text}"
