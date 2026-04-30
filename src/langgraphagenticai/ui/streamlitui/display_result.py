import streamlit as st

class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase=usecase
        self.graph=graph
        self.user_message=user_message

    def display_result_on_ui(self):
        usecase=self.usecase
        graph= self.graph
        user_message =self.user_message
        if usecase=="Basic Chatbot":
            with st.chat_message("user"):
                st.write(user_message)
            for event in graph.stream({"messages": ("user", user_message)}):
                for value in event.values():
                    if value.get("messages"):
                        with st.chat_message("assistant"):
                            st.write(value["messages"][-1].content)
                        



    
    