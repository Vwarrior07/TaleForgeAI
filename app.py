import streamlit as st
from dotenv import load_dotenv
from google.generativeai import GenerativeModel, configure
import os

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
configure(api_key=api_key)

# Model
model = GenerativeModel("models/gemini-2.0-flash")

# UI Setup
st.set_page_config(page_title="TaleForge AI", page_icon="📚")
st.title("📚 TaleForge AI – AI Story Generator")
st.write("Create magical stories powered by Gemini ✨")

# User prompt
prompt = st.text_area(
    "Write a story prompt:",
    placeholder="A young wizard discovers a hidden door in the forest...",
    height=100
)

# Length selector
story_length = st.selectbox(
    "Select story length:",
    [
        "Short (5–7 sentences)",
        "Medium (3–5 paragraphs)",
        "Long (8–12 paragraphs)"
    ],
    index=1
)

# Style selector
story_style = st.selectbox(
    "Select story style:",
    [
        "Fantasy ✨",
        "Romance ❤️",
        "Horror 👻",
        "Comedy 😂",
        "Sci-Fi 🚀",
        "Kids Story 🧸",
        "Mythology 🐉"
    ],
    index=0
)


# Mapping length to instructions
length_map = {
    "Short (5–7 sentences)": "Write a short story of about 5–7 sentences.",
    "Medium (3–5 paragraphs)": "Write a medium-length story of about 3–5 paragraphs.",
    "Long (8–12 paragraphs)": "Write a long, detailed story of about 8–12 paragraphs."
}

# Mapping style to instructions
style_map = {
    "Fantasy ✨": "Write the story in a magical, mythical fantasy style with imaginative world-building.",
    "Romance ❤️": "Write the story in an emotional, heartfelt romantic tone.",
    "Horror 👻": "Write the story in a chilling, dark, suspenseful horror tone.",
    "Comedy 😂": "Write the story in a light-hearted, humorous, funny tone.",
    "Sci-Fi 🚀": "Write the story in a futuristic, scientific, high-tech science fiction tone.",
    "Kids Story 🧸": "Write the story in a simple, cheerful, kid-friendly tone with easy vocabulary.",
    "Mythology 🐉": "Write the story in an epic, legendary, mythological tone inspired by ancient tales."
}

length_instruction = length_map[story_length]

# Generate story button
if st.button("Generate Story"):
    if not prompt.strip():
        st.warning("Please enter a prompt before generating a story.")
    else:

        story_prompt = f"""
        You are an expert creative storyteller.

        Your ONLY job is to write a narrative story.
        Do NOT ask the user questions.
        Do NOT request more details.
        Do NOT generate bullet points.
        Do NOT analyze or explain anything.

        Story Requirements:
        - {length_instruction}
        - Use immersive, emotional, descriptive language.
        - Maintain natural flow and storytelling structure.
        - If character names are missing, create suitable names automatically.
        - Make it engaging and vivid.

        Write the full story based on this prompt:
        "{prompt}"
        """

        with st.spinner("Forging your tale... 🔥"):
            full_prompt = f"{prompt}\n\n{length_instruction}\n{style_map[story_style]}"
            response = model.generate_content(full_prompt)
            story = response.text

        st.subheader("✨ Your Story")
        st.write(story)
