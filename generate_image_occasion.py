import requests
from PIL import Image
from io import BytesIO

# API endpoint URLs
llava_url = "http://8.12.5.48:11434/api/generate"
runwayml_url = "https://api-inference.huggingface.co/models/Adrenex/fastgen"

# Your Hugging Face token for authentication
hugging_face_token = "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"


def generate_image_occasion(occasion, options, user_input, generate_sample):
    modifications = []

    llava_suggestion = ""
    image_bytes = None

    llava_prompt = f"""For the occasion "{occasion}",
    Give suggestions for: {", ".join(options)} based on the person's gender: {user_input}"""

    modified_prompt = llava_prompt
    for mod in modifications:
        modified_prompt += f"\n{mod}"

    llava_payload = {
        "model": "llava:7b-v1.6-mistral-q5_K_M",
        "prompt": modified_prompt,
        "stream": False,
    }

    headers = {"Authorization": f"Bearer {hugging_face_token}"}

    try:
        llava_response = requests.post(llava_url, json=llava_payload, headers=headers)
        llava_response.raise_for_status()  # Raise exception for non-200 status codes

        llava_response_data = llava_response.json()
        llava_suggestion = llava_response_data["response"]

        if generate_sample:  # Check if generate_sample is true
            diffusion_payload = {"inputs": llava_suggestion}
            diffusion_response = requests.post(
                runwayml_url, json=diffusion_payload, headers=headers
            )
            diffusion_response.raise_for_status()  # Raise exception for non-200 status codes

            generated_image = Image.open(BytesIO(diffusion_response.content))
            image_bytes = BytesIO()
            generated_image.save(image_bytes, format="JPEG")
            image_bytes.seek(0)

    except requests.RequestException as e:
        error_message = f"Error accessing the API: {e}"
        print(error_message)
        return None, error_message, generate_sample

    return llava_suggestion, image_bytes, generate_sample
