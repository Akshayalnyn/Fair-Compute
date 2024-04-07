import streamlit as st
from PIL import Image
from suggest_improvements import suggest_improvements
from tempfile import NamedTemporaryFile
import os


def show():
    st.title("Chic Guru \U0001F4A1")

    # File upload widget
    uploaded_file = st.file_uploader(
        "Upload an image of your outfit:",
        type=["jpg", "jpeg", "png"],
    )

    if uploaded_file is not None:
        # Save uploaded file to a temporary location
        with NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        # Create two columns
        col1, col2 = st.columns([1, 3])

        with col1:
            # Display uploaded image on the left side
            st.image(temp_file_path, caption="Uploaded Image", width=100)

        with col2:
            # Call suggest_improvements function
            email = "akshayalnyn@gmail.com"
            password = "akshu2001"
            suggestions = suggest_improvements(temp_file_path, email, password)

            # Display suggestions
            st.title("Level up your style with these tips!")
            st.write(suggestions)

        # Remove the temporary file
        os.remove(temp_file_path)


if __name__ == "__main__":
    show()
