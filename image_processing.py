import base64


def encode_image(image_file):
    """
    Encode the image data into base64 format.

    Args:
    - image_file: Uploaded image file.

    Returns:
    - Base64 encoded image data.
    """
    try:
        encoded_data = base64.b64encode(image_file.read()).decode("utf-8")
        return encoded_data
    except Exception as e:
        print(f"Error encoding image: {e}")
        return None
