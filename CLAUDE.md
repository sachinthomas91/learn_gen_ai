# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a learning repository for Generative AI concepts, featuring example implementations using LangChain, Google Gemini, and Ollama. The repository contains both standalone scripts and interactive Streamlit applications demonstrating various GenAI patterns including basic chat, RAG (Retrieval-Augmented Generation), and prompt engineering.

## Environment Setup

### Python Environment
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# .venv/Scripts/activate   # On Windows

# Install all dependencies
pip install -r requirements.txt
```

### API Keys Configuration
The project uses a `.env` file for API keys. Required keys:
- `GOOGLE_API_KEY`: For Google Gemini models (get from [Google AI Studio](https://makersuite.google.com/app/apikey))

Set environment variables:
```bash
# macOS/Linux
export GOOGLE_API_KEY=your_api_key_here

# Windows (PowerShell)
$env:GOOGLE_API_KEY="your_api_key_here"
```

### Ollama Setup (for local models)
```bash
# Install Ollama from https://ollama.ai/
# Pull the required model
ollama pull qwen2:7b

# Verify Ollama is running
# Default endpoint: http://localhost:11434
```

## Development Commands

### Running Standalone Scripts

**Google Gemini Examples:**
```bash
# Basic Gemini interaction
python langchain/gemini/basic.py

# Interactive chatbot with prompt templates
python langchain/gemini/chatbot.py

# RAG with Gemini and web content
python langchain/gemini/rag.py
```

**Ollama Examples:**
```bash
# Ensure Ollama is running first
# Local chatbot
python langchain/ollama_local/chatbot.py

# RAG with Ollama
python langchain/ollama/rag.py
```

### Running Streamlit Applications

**Chat with Ollama:**
```bash
cd hands_on/streamlit_apps/chat_with_ollama
streamlit run app.py
# Opens at http://localhost:8501
```

**RAG with Gemini:**
```bash
cd hands_on/streamlit_apps/rag_with_gemini
streamlit run app.py
# Opens at http://localhost:8501
```

## Architecture Overview

### Project Structure

```
learn_gen_ai/
├── langchain/              # Standalone LangChain examples
│   ├── gemini/            # Google Gemini integrations
│   │   ├── basic.py       # Simple Q&A with Gemini
│   │   ├── chatbot.py     # Prompt templates and translation
│   │   └── rag.py         # RAG with Chroma + LangGraph
│   ├── ollama/            # Cloud Ollama integrations
│   │   └── rag.py         # RAG with Ollama embeddings
│   └── ollama_local/      # Local Ollama integrations
│       └── chatbot.py     # Translation chatbot
└── hands_on/
    └── streamlit_apps/    # Interactive web applications
        ├── chat_with_ollama/  # Qwen2:7b chat interface
        └── rag_with_gemini/   # Document Q&A with Gemini
```

### Key Architectural Patterns

**LangChain Integration:**
- All examples use LangChain as the orchestration framework
- Model initialization varies by provider (Gemini vs Ollama)
- Common pattern: `init_chat_model()` for provider-agnostic setup

**RAG Implementation:**
- **Vector Store**: Chroma DB for embeddings persistence
  - Gemini: `GoogleGenerativeAIEmbeddings(model="models/embedding-001")`
  - Ollama: `OllamaEmbeddings(model="qwen2:7b")`
- **Document Processing**: `RecursiveCharacterTextSplitter` with 1000 char chunks, 200 char overlap
- **Retrieval**: `similarity_search()` on vector store
- **Graph Orchestration**: LangGraph's `StateGraph` for retrieve → generate workflow
- **Persistence**: Vector stores saved locally (`./chroma_langchain_db`, `./chroma_ollama_db`)

**Streamlit Applications:**
- Session state management for chat history and API keys
- Three document input methods: URL scraping, PDF upload, direct text
- Progress indicators for long-running operations
- Source attribution in RAG responses

### Model Configuration

**Google Gemini:**
- Primary model: `gemini-2.0-flash`
- Embeddings: `models/embedding-001`
- Requires `GOOGLE_API_KEY` environment variable

**Ollama:**
- Primary model: `qwen2:7b`
- Runs locally on port 11434
- No API key required (local inference)

### Vector Store Details

Both RAG implementations use Chroma with local persistence:
- Collections are named by use case (e.g., `example_collection`, `ollama_example_collection`)
- Documents are chunked before embedding
- Stores persist across runs for faster subsequent queries
- Delete persistence directories to rebuild indexes

## Testing & Security

The repository includes security scanning:
```bash
# Security scanning is configured in .github/workflows/security.yml
# Uses bandit and detect-secrets
bandit -r . -f json -o bandit_report.json
detect-secrets scan
```

## Notes for Development

- Python version: 3.12 (specified in `.python-version`)
- All scripts expect API keys via environment variables or runtime prompts
- Streamlit apps include fallback for entering API keys in the UI
- RAG examples use a common blog post URL for testing: https://lilianweng.github.io/posts/2023-06-23-agent/
- LangChain hub prompts are used (`rlm/rag-prompt`) for consistent RAG formatting
