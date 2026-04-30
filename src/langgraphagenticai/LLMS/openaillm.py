import os
import streamlit as st
from langchain_openai import ChatOpenAI


class OpenAILLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            openai_api_key = self.user_controls_input.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
            selected_model = self.user_controls_input.get("selected_model")
            if not openai_api_key:
                st.error("Please enter your OpenAI API Key")
                return None

            llm = ChatOpenAI(api_key=openai_api_key, model=selected_model)

        except Exception as e:
            raise ValueError(f"Error: {str(e)}")
        return llm
