import streamlit as st
from langchain_community.chat_models import ChatOllama


class OllamaLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            selected_model = self.user_controls_input.get("selected_model")
            base_url = self.user_controls_input.get("OLLAMA_BASE_URL") or "http://localhost:11434"

            llm = ChatOllama(model=selected_model, base_url=base_url)

        except Exception as e:
            raise ValueError(f"Error: {str(e)}")
        return llm
