import streamlit as st
from find_similar_image import find_similar_image


def show():
    st.title("MatchMyStyle \U0001F929")
    col1, col2 = st.columns(2)  # Create two columns for layout

    with col1:
        uploaded_image = st.file_uploader(
            "Upload an image", type=["jpg", "jpeg", "png"]
        )
        if uploaded_image is not None:
            st.image(
                uploaded_image, use_column_width=True
            )  # Display original image with column width
            st.write("Original Dress")

    with col2:
        if uploaded_image is not None:
            if st.button("Find Similar Image"):
                similar_image, similarity_score = find_similar_image(uploaded_image)
                similarity_score_percent = round(similarity_score * 100, 2)
                if similar_image:
                    st.write(f"You might like this dress: {similar_image['Link']}")
                    st.write(
                        f"{similarity_score_percent}% similar to your dressing style"
                    )
                    st.markdown(
                        f'<img src="{similar_image["Link"]}" style="height:400px;">',
                        unsafe_allow_html=True,
                    )  # Adjust height here
                    st.write("Suggested Dress")
                else:
                    st.write("No similar image found.")


if __name__ == "__main__":
    show()
