from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

# Initialize the Ollama model
model = ChatOllama(model="qwen2:7b")

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

# Take user input for language and text to translate
language = input("Enter the target language (e.g., Italian, Spanish): ")
text = input("Enter the English text to translate: ")

prompt = prompt_template.invoke(
    {"language": language, "text": text}
)

# Uncomment the following line to see the generated prompt
# print(prompt)

response = model.invoke(prompt)
print(response.content)