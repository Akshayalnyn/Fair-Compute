import os
import streamlit as st
from insta_caption import generate_insta_caption


def show():
    st.title("Instagram Caption Generator")

    # Embedding the Instagram logo with float right and adjusted margin
    st.markdown(
        '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/2048px-Instagram_icon.png" alt="Instagram Logo" style="width: 100px; float: right; margin-top: -70px;">',
        unsafe_allow_html=True,
    )

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Save the uploaded image to a temporary file
        with open("temp_image.jpg", "wb") as f:
            f.write(uploaded_image.getvalue())

        st.image(uploaded_image, caption="Uploaded Image", width=300)

        if st.button("Generate Caption"):
            generated_caption = generate_insta_caption("temp_image.jpg")
            if generated_caption:
                st.info("Generated Caption:")
                st.write(f"{generated_caption}")
                # st.image("phone_outline.png", use_column_width=True)
            else:
                st.warning("Failed to generate caption.")

        # Remove the temporary image file after generating the caption
        os.remove("temp_image.jpg")


if __name__ == "__main__":
    show()
