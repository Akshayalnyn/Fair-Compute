import streamlit as st
from generate_image_occasion import generate_image_occasion


def show():
    st.title("Festive Fashions \U0001F31F")

    occasion = st.text_input("Enter the occasion for dressing up:")
    options = st.multiselect(
        "Select the types of suggestions you want:",
        ["Outfit", "Accessories", "Shoes", "Handbags"],
    )
    user_input = st.text_input("Gender:")
    generate_sample = st.checkbox("Generate Sample Image")
    st.info("This could take time")
    if st.button("Generate Suggestions"):
        llava_suggestion, image_bytes, generate_sample = generate_image_occasion(
            occasion, options, user_input, generate_sample
        )

        if llava_suggestion is not None:
            st.write(f"LLAVA Suggestion: {llava_suggestion}")
            if image_bytes is not None:
                st.image(image_bytes, caption="Generated Image", use_column_width=True)
        else:
            st.error("Model loading. Try after sometime...")
