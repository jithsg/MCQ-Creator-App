import os
import openai
import tiktoken
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.chains import ConversationChain

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_api_key