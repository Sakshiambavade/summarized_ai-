import streamlit as st
from llama_index.llms.groq import Groq
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

# Fetch the API key from the environment variable
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("⚠️ API key is missing! Please set GROQ_API_KEY in your .env file.")
    st.stop()

# Initialize the Groq model
llm = Groq(model="llama3-70b-8192", api_key=api_key)

def summarize_text(text, summary_type):
    prompts = {
        "Normal Summary": f"Summarize the following text:\n{text}",
        "Short Summary": f"Summarize the following text in 10 words:\n{text}",
        "Simple Summary": f"Summarize the following text in layman terms:\n{text}",
        "Bullet Point Summary": f"Summarize the following text in 3 bullet points:\n{text}",
    }

    prompt = prompts.get(summary_type, f"Summarize the text:\n{text}")

    # Use llm.predict() instead of the incorrect complete()
    try:
        response = llm.predict(prompt)
        return response
    except Exception as e:
        return f"⚠️ Error generating summary: {str(e)}"

# Streamlit app
st.title("📄 AI-Powered Text Summarizer 🤖")

# Text input area
text = st.text_area("Enter a large text paragraph", height=200)

# Summary Type Selection
summary_type = st.selectbox(
    "Select Summary Type",
    ("Normal Summary", "Short Summary", "Simple Summary", "Bullet Point Summary")
)

# Button to generate summary
if st.button("Generate Summary"):
    if text.strip():
        with st.spinner("Generating summary... ⏳"):
            summary = summarize_text(text, summary_type)
            st.subheader(f"📜 {summary_type}")
            st.write(summary)
    else:
        st.warning("⚠️ Please enter some text to summarize.")

# Footer
st.markdown("---")
st.markdown("🚀 Made by **Sakshi Ambavade**")
