import streamlit as st
from based_on_country import generate_country_suggestion


def show():
    st.title("Fashion Voyage \U0001F30D")

    country_name = st.text_input(
        "Enter the name of the country you want to dress like:"
    )
    gender = st.selectbox("Select your gender:", ["Male", "Female", "Non-binary"])

    if st.button("Generate Suggestions"):
        with st.spinner("Generating Suggestions..."):
            llava_suggestion, generated_image = generate_country_suggestion(
                country_name, gender
            )

        if llava_suggestion is not None:
            st.write(f"LLAVA Suggestion: {llava_suggestion}")

        if generated_image is not None:
            st.write("Generated Image:")
            st.image(generated_image, caption="Generated Fashion Style")

    return country_name, gender


if __name__ == "__main__":
    show()
