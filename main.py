import streamlit as st
from llama_index.llms.groq import Groq
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

# Fetch the API key from the environment variable
api_key = os.getenv("GROQ_API_KEY")

# Initialize the Groq model
llm = Groq(model="llama3-70b-8192", api_key=api_key)

def summarize_text(text, summary_type):
    if summary_type == "Normal Summary":
        prompt = f"Summarize the text: {text}"
    elif summary_type == "Short Summary":
        prompt = f"Summarize the text in 10 words: {text}"
    elif summary_type == "Simple Summary":
        prompt = f"Summarize the text in layman terms: {text}"
    elif summary_type == "Bullet Point Summary":
        prompt = f"Summarize the text in 3 bullet points: {text}"

    response = llm.complete(prompt)
    return response

# Streamlit app
st.title("📄 Text Summarizer 🤖")

# Text input area
text = st.text_area("Enter a large text paragraph")

# Buttons for different summaries
if st.button("Normal Summary 💡"):
    if text:
        summary = summarize_text(text, "Normal Summary")
        st.write("### Normal Summary 💡")
        st.write(summary)
    else:
        st.write("Please enter some text to summarize.")

if st.button("Short Summary 💬"):
    if text:
        summary = summarize_text(text, "Short Summary")
        st.write("### Short Summary 💬")
        st.write(summary)
    else:
        st.write("Please enter some text to summarize.")

if st.button("Simple Summary 🔖"):
    if text:
        summary = summarize_text(text, "Simple Summary")
        st.write("### Simple Summary 🔖")
        st.write(summary)
    else:
        st.write("Please enter some text to summarize.")

if st.button("Bullet Point Summary 🎯"):
    if text:
        summary = summarize_text(text, "Bullet Point Summary")
        st.write("### Bullet Point Summary 🎯")
        st.write(summary)
    else:
        st.write("Please enter some text to summarize.")

# Add a footer
st.markdown("---")
st.markdown("Made by Sakshi Ambavade")
