import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Start
st.set_page_config(page_title="RCW Chat", page_icon="book", layout="wide")
st.title("Streaming Chatbot")

def retrieve_response(user_input, chat_history):
    template = """
    You are a helpful assistant. YOU MUST answer the following questions considering the
    history of the conversation:
    Chat history: {chat_history}
    User question: {user_question}
    
    """
    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI(model="gpt-4o", max_tokens=2500)
    chain = prompt | llm | StrOutputParser()
    return chain.stream({
        "chat_history": chat_history,
        "user_question": user_input 
    })
    
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hey there, I am Cassandra. How can I be of service to you?")
    ]
   
# Conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

# User input
user_query = st.chat_input("How can Cassandra help?")
if user_query is not None and user_query!= "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    with st.chat_message("Human"):
        st.markdown(user_query)
    with st.chat_message("AI"):
        response = st.write_stream(retrieve_response(user_query, st.session_state.chat_history))
    
    st.session_state.chat_history.append(AIMessage(content=response))
        

        
