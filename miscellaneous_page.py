import os
import streamlit as st
from miscellaneous import generate_answer


def show():
    st.title("Image-Based Question Answering")
    question = st.text_input("Ask your question:")

    # Upload image button on the right
    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "png"],
        key="image_upload",
        help="Upload an image to generate an answer.",
    )

    # Flag to track if answer has been generated
    answer_generated = False

    if uploaded_file is not None and question:
        # Save the uploaded image temporarily
        temp_image_path = "temp_image.jpg"
        with open(temp_image_path, "wb") as f:
            f.write(uploaded_file.read())

        # Generate answer if Regenerate Answer button is clicked
        if st.button("Generate Answer"):
            answer_generated = True
            answer = generate_answer(question, temp_image_path)

            # Display the answer on the website
            st.write("Answer:", answer)

        # Remove the temporary image file
        os.remove(temp_image_path)

    return question, uploaded_file, answer_generated
