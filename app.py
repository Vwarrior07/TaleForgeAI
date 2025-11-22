import streamlit as st
from dotenv import load_dotenv
from google.generativeai import GenerativeModel, configure
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

configure(api_key=api_key)

model = GenerativeModel("models/gemini-2.0-flash")



st.set_page_config(page_title="TaleForge AI", page_icon="📚")
st.title("📚 TaleForge AI – AI Story Generator")
st.write("Create magical stories powered by Gemini ✨")

prompt = st.text_area("Write a story prompt:", placeholder="A young wizard discovers a hidden door in the forest...")

story_length = st.selectbox(
    "Select story length:",
    ["Short (1 paragraph)", "Medium (3–5 paragraphs)", "Long (8–12 paragraphs)"],
    index=1
)

if st.button("Generate Story"):
    if not prompt.strip():
        st.warning("Please enter a prompt before generating a story.")
    else:
        with st.spinner("Forging your tale... 🔥"):
            response = model.generate_content(prompt)
            story = response.text

        st.subheader("✨ Your Story")
        st.write(story)
