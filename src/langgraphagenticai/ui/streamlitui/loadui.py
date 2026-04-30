import streamlit as st
from src.langgraphagenticai.ui.uiconfigfile import Config
import os

CUSTOM_CSS = """
<style>
/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1A1D2E 0%, #0E1117 100%);
    border-right: 1px solid #6C63FF33;
}
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stTextInput label {
    color: #CCCCDD !important;
    font-size: 0.82rem;
}

/* ── Sidebar brand block ── */
.sidebar-brand {
    text-align: center;
    padding: 0.75rem 0 0.25rem 0;
}
.sidebar-brand h2 {
    color: #6C63FF;
    font-size: 1.15rem;
    font-weight: 700;
    margin: 0 0 0.2rem 0;
    letter-spacing: -0.01em;
}
.sidebar-brand p {
    color: #666;
    font-size: 0.72rem;
    margin: 0;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

/* ── Section labels ── */
.section-label {
    color: #6C63FF;
    font-size: 0.68rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin: 0 0 0.4rem 0;
}

/* ── Active config card ── */
.config-card {
    background: #6C63FF11;
    border: 1px solid #6C63FF33;
    border-radius: 8px;
    padding: 0.65rem 0.8rem;
    font-size: 0.78rem;
    color: #aaa;
    line-height: 1.7;
}
.config-card b { color: #6C63FF; }

/* ── Main hero ── */
.hero {
    background: linear-gradient(135deg, #6C63FF18 0%, #0E1117 60%);
    border: 1px solid #6C63FF33;
    border-radius: 16px;
    padding: 2.5rem 2rem 2rem 2rem;
    text-align: center;
    margin-bottom: 2rem;
}
.hero h1 {
    font-size: 2.1rem;
    font-weight: 800;
    margin: 0 0 0.5rem 0;
    background: linear-gradient(90deg, #6C63FF, #a89cff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero p {
    color: #888;
    font-size: 0.95rem;
    margin: 0;
}

/* ── Feature cards ── */
.feature-card {
    background: #1A1D2E;
    border: 1px solid #6C63FF22;
    border-radius: 12px;
    padding: 1.2rem 1rem;
    text-align: center;
    height: 100%;
    transition: border-color 0.2s;
}
.feature-card:hover { border-color: #6C63FF88; }
.feature-card .icon { font-size: 1.8rem; margin-bottom: 0.5rem; }
.feature-card h4 {
    color: #EEEEFF;
    font-size: 0.9rem;
    font-weight: 600;
    margin: 0 0 0.3rem 0;
}
.feature-card p {
    color: #666;
    font-size: 0.78rem;
    margin: 0;
    line-height: 1.5;
}
</style>
"""

FEATURES = [
    ("💬", "Basic Chatbot", "Conversational AI with persistent state across turns"),
    ("🔧", "Chatbot with Tools", "Agents that call external tools and APIs"),
    ("📰", "AI News", "Fetch and summarise the latest news automatically"),
    ("✍️", "Blog Generator", "Generate well-structured blog posts on any topic"),
]


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(
            page_title=self.config.get_page_title(),
            layout="wide",
            page_icon="🧠",
        )
        st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

        # ── Hero header ──
        st.markdown("""
        <div class="hero">
            <h1>🧠 LangGraph Agentic AI</h1>
            <p>Build and interact with stateful AI agents powered by LangGraph</p>
        </div>
        """, unsafe_allow_html=True)

        # ── Feature cards ──
        cols = st.columns(len(FEATURES), gap="medium")
        for col, (icon, title, desc) in zip(cols, FEATURES):
            with col:
                st.markdown(f"""
                <div class="feature-card">
                    <div class="icon">{icon}</div>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>
                """, unsafe_allow_html=True)

        st.write("")  # spacing before chat

        # ── Sidebar ──
        with st.sidebar:
            st.markdown("""
            <div class="sidebar-brand">
                <h2>⚡ AgenticAI Studio</h2>
                <p>Powered by LangGraph</p>
            </div>
            """, unsafe_allow_html=True)
            st.divider()

            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            st.markdown('<p class="section-label">🤖 Model Configuration</p>', unsafe_allow_html=True)

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox(
                "Select LLM",
                options=llm_options,
                index=0,
                key="selected_llm"
            )

            if self.user_controls["selected_llm"] == "Groq":
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_model"] = st.selectbox(
                    "Select Model",
                    options=model_options,
                    index=0,
                    key="selected_model"
                )
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input(
                    "API Key", type="password", key="groq_api_key"
                )
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your Groq API Key")
                else:
                    os.environ["GROQ_API_KEY"] = self.user_controls["GROQ_API_KEY"]
                    st.success("API Key configured")

            elif self.user_controls["selected_llm"] == "OpenAI":
                model_options = self.config.get_openai_model_options()
                self.user_controls["selected_model"] = st.selectbox(
                    "Select Model",
                    options=model_options,
                    index=0,
                    key="selected_model"
                )
                self.user_controls["OPENAI_API_KEY"] = st.session_state["OPENAI_API_KEY"] = st.text_input(
                    "API Key", type="password", key="openai_api_key"
                )
                if not self.user_controls["OPENAI_API_KEY"]:
                    st.warning("Please enter your OpenAI API Key")
                else:
                    os.environ["OPENAI_API_KEY"] = self.user_controls["OPENAI_API_KEY"]
                    st.success("API Key configured")

            elif self.user_controls["selected_llm"] == "Ollama":
                model_options = self.config.get_ollama_model_options()
                self.user_controls["selected_model"] = st.selectbox(
                    "Select Model",
                    options=model_options,
                    index=0,
                    key="selected_model"
                )
                self.user_controls["OLLAMA_BASE_URL"] = st.text_input(
                    "Ollama Base URL (optional)",
                    value="http://localhost:11434",
                    key="ollama_base_url"
                )
                st.info("Ollama runs locally — no API key required. Ensure Ollama is running on the base URL above.")

            st.divider()
            st.markdown('<p class="section-label">🎯 Use Case</p>', unsafe_allow_html=True)

            # Use case selection
            self.user_controls["selected_usecase"] = st.selectbox(
                "Select Use Case",
                options=usecase_options,
                index=0,
                key="selected_usecase"
            )

            st.divider()

            # Active config summary
            if self.user_controls.get("selected_model"):
                st.markdown(f"""
                <div class="config-card">
                    <b>Active Config</b><br>
                    Provider: {self.user_controls["selected_llm"]}<br>
                    Model: {self.user_controls["selected_model"]}<br>
                    Use Case: {self.user_controls["selected_usecase"]}
                </div>
                """, unsafe_allow_html=True)

        return self.user_controls
