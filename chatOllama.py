from langchain_ollama import OllamaLLM
import time

model = OllamaLLM(model="mistral")
user_input = "C'est quoi la difference entre un idiot et un con?"
result = model.invoke(user_input)

for char in result: # Iterate over each character in the full response
    print(char, end="", flush=True)
    time.sleep(0.02)
print() # New line after streaming for a smoother effect

# print(result)