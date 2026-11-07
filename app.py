import streamlit as st
from translator import translate_text
# Page configuration
st.set_page_config(
    page_title="LinguaBridge",
    page_icon="🌍",
    layout="centered"
)

# Application title
st.title("🌍 LinguaBridge")
st.subheader("Your Smart Language Translator")

st.write("Translate text between different languages easily.")

# Language selection
languages = [
    "English",
    "Tamil",
    "Hindi",
    "French",
    "German",
    "Spanish",
    "Japanese"
]

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox("From", languages)

with col2:
    target = st.selectbox("To", languages, index=1)

# Text input
user_text = st.text_area(
    "Enter your text",
    placeholder="Type something to translate..."
)

# Translate button
if st.button("🌐 Translate", use_container_width=True):
    if not user_text.strip():
        st.warning("Please enter some text.")

    elif source == target:
        st.warning("Please select different languages.")

    else:
        try:
            with st.spinner("Translating..."):
                result = translate_text(
                    user_text,
                    source,
                    target
                )

            st.success("Translation completed!")
            st.subheader("Translated Text")
            st.write(result)

        except Exception as e:
            st.error(f"Translation failed: {e}")


st.caption("Powered by LinguaBridge")