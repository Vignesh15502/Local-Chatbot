from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

st.title("Vignesh Chat Bot")
input_txt = st.text_input("Plese enter your queries here...")

prompt = ChatPromptTemplate.from_messages(
    [("system","You are a helpful AI Assistant. Your name is Rami"),
     ("user", "user query:{query}")]
)

llm = Ollama(model = "llama3.2-vision:latest")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_txt:
    st.write(chain.invoke({"query":input_txt}))