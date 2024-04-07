import requests
import time
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

llava_url = "http://8.12.5.48:11434/api/generate"
hugging_face_token = "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"


def generate_country_suggestion(country_name, gender):
    # Add country and gender information to the LLAVA prompt
    llava_prompt = f"""For the given country and gender: {country_name}, {gender}, generate appropriate dress and accessories.

    User selected options: outfit"""

    # Payload data for LLAVA model without image input
    llava_payload = {
        "model": "llava:7b-v1.6-mistral-q5_K_M",
        "prompt": llava_prompt,
        "stream": False,
    }

    # Headers with Hugging Face token for authentication
    headers = {"Authorization": f"Bearer {hugging_face_token}"}

    # Send POST request to LLAVA model with authentication headers
    llava_response = requests.post(llava_url, json=llava_payload, headers=headers)

    # Check response status from LLAVA model
    if llava_response.status_code == 200:
        # Get the LLAVA model's response
        llava_response_data = llava_response.json()
        llava_suggestion = llava_response_data["response"]
        print("LLAVA Suggestion:", llava_suggestion)

        # Generate image using Hugging Face model
        generated_image_data = generate_image(hugging_face_token, llava_suggestion)
        if generated_image_data:
            print("Image generated successfully!")
            generated_image = Image.open(BytesIO(generated_image_data))
            return llava_suggestion, generated_image
        else:
            print("Error generating image with Hugging Face model.")
    else:
        print(
            f"Error accessing the LLAVA model: {llava_response.status_code} - {llava_response.text}"
        )

    # Wait for a few seconds before next iteration to avoid frequent requests
    time.sleep(5)


def generate_image(hugging_face_token, inputs):
    hugging_face_url = "https://api-inference.huggingface.co/models/Adrenex/fastgen"
    headers = {"Authorization": f"Bearer {hugging_face_token}"}
    payload = {"inputs": inputs}

    response = requests.post(hugging_face_url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.content
    else:
        print(
            f"Error generating image with Hugging Face model: {response.status_code} - {response.text}"
        )
        return None


# Example usage
country_name = "India"
gender = "Male"
llava_suggestion, generated_image = generate_country_suggestion(country_name, gender)

# Display LLAVA suggestion and generated image
if llava_suggestion:
    print("LLAVA Suggestion:", llava_suggestion)

if generated_image:
    plt.imshow(generated_image)
    plt.axis("off")
    plt.show()
