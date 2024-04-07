import streamlit as st


def main():
    # Set page background color to lavender
    st.markdown(
        """
        <style>
            body {
                background-color: lavender;
            }
            .smartglam-text {
                font-size: 45px;
                font-weight: bold;
                color: #967BB6;
            }
            .tagline-text {
                font-size: 22px;
                font-style: italic;
                color: #808080; /* Slightly darker grey */
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display SmartGlam text
    st.markdown(
        '<div class="smartglam-text">Welcome to SmartGlam \U0001F483 \U0001F57A</div>',
        unsafe_allow_html=True,
    )

    # Display tagline text
    st.markdown(
        '<div class="tagline-text">Your Fashion Assistant...</div><br><br>',
        unsafe_allow_html=True,
    )

    # Create sidebar navigation
    selection = st.sidebar.radio(
        "How can I help you?",
        (
            "Generate Description",
            "Suggest Improvements",
            "What occasion is this for?",
            "Help me dress for this occasion",
            "Find Similar dress",
            "Dress based on country",
            "Generate Instagram caption",
            "Miscellaneous",
        ),
    )

    # Render selected feature
    if selection == "Generate Description":
        import generate_description_page

        generate_description_page.show()
    elif selection == "Suggest Improvements":
        import suggest_improvements_page

        suggest_improvements_page.show()
    elif selection == "What occasion is this for?":
        import occasion_suggestions_page

        occasion_suggestions_page.show()
    elif selection == "Help me dress for this occasion":
        import generate_image_occasion_page

        generate_image_occasion_page.show()
    elif selection == "Find Similar dress":
        import similar_image_finder_page

        similar_image_finder_page.show()
    elif selection == "Dress based on country":
        import based_on_country_page

        based_on_country_page.show()
    elif selection == "Generate Instagram caption":
        import insta_caption_page

        insta_caption_page.show()
    elif selection == "Miscellaneous":
        import miscellaneous_page

        miscellaneous_page.show()


if __name__ == "__main__":
    main()
