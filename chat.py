from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import time
template = """
You are my helpful assistant. Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# model = OllamaLLM(model="llama3.2")
# # result = model.invoke("Talk to me about Maslow's pyramid")
# prompt = ChatPromptTemplate.from_template(template)
# chain = prompt | model
# # res = ""
# # for i in result:
# #     res += i
# #     print(res, end = " ")

# result = chain.invoke({"context": "", "question": "Hey how are you?"})
# print(result)

model = OllamaLLM(model="llama3.2")
# result = model.invoke("Talk to me about Maslow's pyramid")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
# res = ""
# for i in result:
#     res += i
#     print(res, end = " ")

def handle_conversation():
    context = ""
    print("Welcome to the AI ChatBot! Provide a question or type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        result = chain.invoke({"context": context, "question": user_input})
        res = ""
        print("Bot: ", end="")

        for char in result:  # Iterate over each character in the full response
            res += char
            print(char, end="", flush=True)
            time.sleep(0.05)  # Adjust the delay for a smoother effect

        print()  # Newline after the streaming is complete

                
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == '__main__':
    handle_conversation()