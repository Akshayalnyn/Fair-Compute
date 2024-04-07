import streamlit as st
from PIL import Image
from io import BytesIO
from occasion_suggestions import get_occasion_suggestions
import base64


def show():
    st.title("Event Enchanter \U0001F389")

    # File upload widget
    uploaded_file = st.file_uploader(
        "Upload a picture of your outfit:",
        type=["jpg", "jpeg", "png"],
    )

    if uploaded_file is not None:
        # Save uploaded file to a temporary location
        with BytesIO() as temp_buffer:
            temp_buffer.write(uploaded_file.read())
            temp_buffer.seek(0)
            image_data = base64.b64encode(temp_buffer.read()).decode()

        # Create columns layout
        col1, col2 = st.columns([1, 3])

        # Display uploaded image in the first column
        with col1:
            st.image(
                Image.open(BytesIO(base64.b64decode(image_data))),
                caption="Uploaded Image",
                use_column_width=True,
            )

        # Call function to get occasion suggestions
        suggestions = get_occasion_suggestions(image_data)

        # Display suggestions in the second column
        with col2:
            st.write(suggestions)


if __name__ == "__main__":
    show()
