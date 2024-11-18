from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import time


template = """
You are my helpful assistant. Answer the following questions considering the history.

Actively engage with the user by offering helpful suggestions and taking initiative to solve their problems. 
Ensure your responses are compassionate and empathetic, acknowledging the user's feelings and perspectives.

Note: by empath 

Here is the conversation history: {context}

Question: {question}

Answer:

"""
model = OllamaLLM(model="mistral")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
def handleConversation():
    context = ""
    print("Hi, I am cassandra, how can I be of service to you today? Should you have no question, please type ''quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        result = chain.invoke({"context": context, "question": user_input})
        for char in result: # Iterate over each character in the full response
            print(char, end="", flush=True)
            time.sleep(0.02)
        print() # New line after streaming for a smoother effect
        context += f"\nUser: {user_input}\nAI: {result}"
if __name__ == '__main__':
    handleConversation()