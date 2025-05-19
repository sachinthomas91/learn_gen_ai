# LangChain Gemini Example

This project demonstrates how to use the `langchain_google_genai` library to interact with Google's Gemini model using LangChain in Python.

## Prerequisites
- Python 3.8+
- `langchain_google_genai` package
- Google API Key for Gemini

## Setup

1. **Install dependencies**
   
   You can install the required package using pip:
   ```bash
   pip install langchain-google-genai
   ```

2. **Set your Google API Key**
   
   You need to set the `GOOGLE_API_KEY` environment variable so the script can authenticate with Gemini. You can do this in your terminal:
   
   **On Windows (Command Prompt):**
   ```cmd
   set GOOGLE_API_KEY=your_api_key_here
   ```
   **On Windows (PowerShell):**
   ```powershell
   $env:GOOGLE_API_KEY="your_api_key_here"
   ```
   **On Linux/macOS (bash):**
   ```bash
   export GOOGLE_API_KEY=your_api_key_here
   ```

3. **Run the script**
   
   ```bash
   python langchain_base.py
   ```

## Example Code

The script sends a prompt to Gemini and prints the response. See `langchain_base.py` for details.

---

## License
MIT
