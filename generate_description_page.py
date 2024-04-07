import streamlit as st
from PIL import Image
from io import BytesIO
from generate_description import generate_description


def show():
    st.title("Fashion Fineprint \U0001F4DD")

    # File upload widget
    uploaded_file = st.file_uploader(
        "Upload an image of your outfit:", type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image_data = uploaded_file.read()

        # Display uploaded image and description side by side
        st.write(
            "<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>",
            unsafe_allow_html=True,
        )
        col1, col2 = st.columns([1, 3])  # Create two columns

        with col1:
            # Display uploaded image on the left side
            st.image(
                Image.open(BytesIO(image_data)), caption="Uploaded Image", width=300
            )

        with col2:
            # Generate description and display on the right side
            description = generate_description(image_data)
            st.write(
                f'<div style="padding-left: 120px;">{description}</div>',
                unsafe_allow_html=True,
            )
