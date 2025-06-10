import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

# Ensure that the GOOGLE_API_KEY environment variable is set
if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")
  
# Initialize the Google Gemini 2.0 flash model
model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

# # Option 1: Using the Google Gemini chat model with LangChain
# # If you want to use the Google Gemini chat model directly, you can uncomment the following lines:
# messages = [
#     SystemMessage("Translate the following from English into Italian"),
#     HumanMessage("hi!"),
# ]

# response = model.invoke(messages)
# print(response)  # Print the model's response
    
# # Option 2: Using the Google Gemini Prompt Template with LangChain
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