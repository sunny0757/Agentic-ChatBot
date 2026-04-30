import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.LLMS.openaillm import OpenAILLM
from src.langgraphagenticai.LLMS.ollamallm import OllamaLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Load and runs the Langgraph Agentic AI App with streamlit UI.
    This funcation initalizes the UI,handles usr input, configus the llm model,set up the graph
    the graph and finally run the application.
    """
    ##Load UI
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("No input")
        return

    user_message = st.chat_input("Enter your message")

    if user_message:
        try:
            # Configure LLM based on selected provider
            selected_llm = user_input.get("selected_llm")
            if selected_llm == "OpenAI":
                obj_llm_config = OpenAILLM(user_input)
            elif selected_llm == "Ollama":
                obj_llm_config = OllamaLLM(user_input)
            else:
                obj_llm_config = GroqLLM(user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Failed to Configure LLM")
                return

            # Initialize and set up the graph based on use case
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("No usecase selected")
                return

        except Exception as e:
            st.error(f"Error configuring LLM: {str(e)}")
            return
        ## Graph Builder

        graph_builder=GraphBuilder(model)
        try:
            graph=graph_builder.setup_graph(usecase)
            DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
        except Exception as e:
            st.error(f"Error setting up graph: {str(e)}")
            return
            

        
        
    