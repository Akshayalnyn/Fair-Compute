import base64
import os
import requests
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

llava_url = "http://8.12.5.48:11434/api/generate"
hugging_face_token = "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"


def preprocess_text(text):
    # Remove non-alphanumeric characters
    text = "".join(e for e in text if e.isalnum() or e.isspace())
    # Convert to lowercase and tokenize
    tokens = text.lower().split()
    return " ".join(tokens)


def generate_llava_description(image_data):
    try:
        # Payload data for LLAVA model with image input
        llava_payload = {
            "model": "llava:7b-v1.6-mistral-q5_K_M",
            "prompt": f"Generate a description for this image",
            "stream": False,
            "images": [image_data],
        }
        # Headers with Hugging Face token for authentication
        headers = {"Authorization": f"Bearer {hugging_face_token}"}

        # Send POST request to LLAVA model with authentication headers
        llava_response = requests.post(llava_url, json=llava_payload, headers=headers)
        llava_response.raise_for_status()  # Raise an error if response status is not 200

        llava_response_data = llava_response.json()
        description = llava_response_data["response"]
        return description
    except requests.exceptions.RequestException as e:
        print(f"Error generating LLAVA description: {e}")
        return None


def find_similar_image(uploaded_image):
    # Load existing descriptions from CSV
    csv_file = os.getcwd() + "/final_image_descriptions.csv"
    existing_descriptions_df = pd.read_csv(csv_file, encoding="utf-8")

    # Preprocess descriptions for similarity calculation
    existing_descriptions_df["Preprocessed_description"] = existing_descriptions_df[
        "Description"
    ].apply(preprocess_text)

    # Encode the uploaded image with base64
    uploaded_image_data = uploaded_image.read()
    uploaded_image_base64 = base64.b64encode(uploaded_image_data).decode("utf-8")

    # Convert the uploaded image to a description using LLAVA or other methods
    user_image_description = generate_llava_description(uploaded_image_base64)
    if user_image_description:
        user_description_preprocessed = preprocess_text(user_image_description)
    else:
        return None, None  # Handle failure to generate description

    most_similar_image = None
    highest_similarity = 0.0
    vectorizer = TfidfVectorizer()

    # Iterate through existing descriptions and find the most similar image
    for index, row in existing_descriptions_df.iterrows():
        existing_description = row["Preprocessed_description"]
        similarity = cosine_similarity(
            vectorizer.fit_transform(
                [existing_description, user_description_preprocessed]
            )
        )[0][1]
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_image = {
                "ID": row["ID"],
                "Link": row["Link"],
                "Description": existing_description,
            }

    return most_similar_image, highest_similarity
