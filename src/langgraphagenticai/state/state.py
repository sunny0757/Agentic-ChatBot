from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class State(TypedDict):
    """
    Represent the state of the graph.

    """
    messages: Annotated[list, add_messages]
    


    