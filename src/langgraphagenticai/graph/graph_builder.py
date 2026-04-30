from langgraph.graph import StateGraph,END,START
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Build a simple chatbot graph using Langgraph.
        This method initializes a chatbot node using "BasicChatbotNode" class and
        adds it to the graph builder. This chatbot node is set as both entry and exit
        point of the graph.

        """
        self.chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        
    def setup_graph(self,usecase):
        """
        Set up the graph based on the use case.
        This method selects the appropriate graph builder method based on the use case
        and returns the compiled graph.
        """
        if usecase=="Basic Chatbot":
            self.basic_chatbot_build_graph()
            return self.graph_builder.compile()
        else:
            raise ValueError(f"Unknown usecase: {usecase}")






    
        
    