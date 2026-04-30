from src.langgraphagenticai.state.state import State


class BasicChatbotNode:
    """
    Basic chatbot node that can be used to build a simple chatbot graph.

    """
    def __init__(self,model):
        self.llm=model

    def process(self,state:State)->dict:
        """
        Process the input message and return the response.
        
        

        """
        return {"messages": [self.llm.invoke(state["messages"])]}


    
