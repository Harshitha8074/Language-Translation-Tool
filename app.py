import streamlit as st
from googletrans import Translator, LANGUAGES
import streamlit.components.v1 as components

t = Translator()

st.title("🌍 Language Translator")

text = st.text_input("Enter Text")

src = st.selectbox("From Language", list(LANGUAGES.keys()))
dest = st.selectbox("To Language", list(LANGUAGES.keys()))


if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter text")
    else:
        result = t.translate(text, src=src, dest=dest).text

        st.success("Translation:")
        st.write(result)

        
        st.session_state["result"] = result

        st.code(result)
        st.text_area("Copy Text", result)


