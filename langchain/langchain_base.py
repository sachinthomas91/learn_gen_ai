# This script demonstrates how to use LangChain with Google's Gemini model.
# It sends a prompt to Gemini and prints the response.
#
# Prerequisites:
# - Install langchain-google-genai: pip install langchain-google-genai
# - Set your Google API key in the environment variable 'GOOGLE_API_KEY'.
#
# How to set the API key from terminal:
#   On Windows (Command Prompt):
#       set GOOGLE_API_KEY=your_api_key_here
#   On Windows (PowerShell):
#       $env:GOOGLE_API_KEY="your_api_key_here"
#   On Linux/macOS (bash):
#       export GOOGLE_API_KEY=your_api_key_here
#
# Replace 'your_api_key_here' with your actual API key.

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=os.environ["GOOGLE_API_KEY"])
response = llm.invoke([HumanMessage(content="What's the capital of France?")])
print(response.content)
