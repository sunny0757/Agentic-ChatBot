from configparser import ConfigParser
import os


class Config:
    def __init__(self, Config_file=None):
        self.config = ConfigParser()
        if Config_file is None:
            Config_file = os.path.join(os.path.dirname(__file__), "uiconfigfile.ini")
        self.config.read(Config_file)
    
    def get_llm_options(self):
        return [x.strip() for x in self.config["DEFAULT"].get("LLM_OPTIONS").split(",")]

    def get_usecase_options(self):
        return [x.strip() for x in self.config["DEFAULT"].get("USECASE_OPTIONS").split(",")]

    def get_groq_model_options(self):
        return [x.strip() for x in self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(",")]

    def get_openai_model_options(self):
        return [x.strip() for x in self.config["DEFAULT"].get("OPENAI_MODEL_OPTIONS").split(",")]

    def get_ollama_model_options(self):
        return [x.strip() for x in self.config["DEFAULT"].get("OLLAMA_MODEL_OPTIONS").split(",")]

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
         

        
        
        