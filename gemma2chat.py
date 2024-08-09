from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

os.environ["LANGCHAIN_TRACING-V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Prompt templates
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question:{question}")
    ]
)

# Streamlit UI
st.title('CHATBOT USING gemma2 model')

# Adding custom CSS for blue to black gradient background
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, blue, black);
        color: white;  /* Optional: Change text color to white for better readability */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Text input
input_text = st.text_input("Search the topic you want")

# Ollama gemma2 LLM
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Display output
if input_text:
    st.write(chain.invoke({"question": input_text}))
