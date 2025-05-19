# learn_gen_ai

This repository is a collection of resources, code samples, and hands-on projects for learning about Generative AI (GenAI) and related technologies. It is organized to help beginners and practitioners explore GenAI concepts, tools, and real-world applications.

## Repository Structure

- **learn_gen_ai/**: Main directory for GenAI learning resources and code.
  - **hands_on/langchain/**: Example scripts and guides for using LangChain with models like Gemini.
  - **README.md**: Instructions and explanations for each submodule

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/learn_gen_ai.git
   cd learn_gen_ai
   ```

2. **Set up a Python environment**
   - Use the provided `venv-genai` or create a new virtual environment:
     ```bash
     python -m venv venv-genai
     source venv-genai/Scripts/activate  # On Windows
     # or
     source venv-genai/bin/activate      # On Linux/macOS
     ```

3. **Install dependencies**
   - Navigate to the relevant project folder (e.g., `learn_gen_ai/hands_on/langchain/`) and install requirements as needed:
     ```bash
     pip install -r requirements.txt
     # or for specific modules:
     pip install langchain-google-genai
     ```

4. **Set up API keys**
   - For scripts using external APIs (e.g., Gemini), set the required environment variables as described in the respective README files.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements, new examples, or corrections.

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.
