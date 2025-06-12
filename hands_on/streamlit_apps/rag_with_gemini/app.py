import streamlit as st
import getpass
import os
import bs4
import tempfile
from langchain import hub
from langchain_chroma import Chroma
from typing_extensions import List, TypedDict
from langchain_core.documents import Document
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Page config
st.set_page_config(page_title="RAG with Gemini", layout="wide")
st.title("📚 RAG with Google Gemini")

# Initialize session state for vector store
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

# Sidebar for API key
with st.sidebar:
    if os.environ.get("GOOGLE_API_KEY"):
        use_existing = st.checkbox("Use existing API key", value=True)
        if not use_existing:
            api_key = st.text_input("Enter new Google API Key", type="password")
            if api_key:
                os.environ["GOOGLE_API_KEY"] = api_key
        else:
            api_key = os.environ["GOOGLE_API_KEY"]
    else:
        api_key = st.text_input("Enter Google API Key", type="password")
        if api_key:
            os.environ["GOOGLE_API_KEY"] = api_key

    st.markdown("### Instructions")
    st.markdown("""
    1. Enter your Google API key
    2. Choose input method
    3. Add your document
    4. Ask questions about the content
    """)

# Initialize models if API key is provided
if api_key:
    llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    # Document input section
    st.markdown("### 📄 Document Input")
    input_method = st.radio(
        "Choose input method:",
        ["URL", "PDF Upload", "Text Input"]
    )

    # Handle different input methods
    if input_method == "URL":
        url = st.text_input("Enter URL:")
        if url and st.button("Load URL"):
            with st.spinner("Loading and processing URL content..."):
                loader = WebBaseLoader(
                    web_paths=(url,),
                    bs_kwargs=dict(
                        parse_only=bs4.SoupStrainer(
                            class_=("post-content", "post-title", "post-header")
                        )
                    )
                )
                docs = loader.load()
                st.success("URL content loaded successfully!")

    elif input_method == "PDF Upload":
        uploaded_file = st.file_uploader("Upload PDF", type=['pdf'])
        if uploaded_file and st.button("Process PDF"):
            with st.spinner("Processing PDF..."):
                # Save uploaded file temporarily
                with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_path = tmp_file.name
                
                loader = PyPDFLoader(tmp_path)
                docs = loader.load()
                os.unlink(tmp_path)  # Remove temporary file
                st.success("PDF processed successfully!")

    else:  # Text Input
        text_input = st.text_area("Enter your text:")
        if text_input and st.button("Process Text"):
            with st.spinner("Processing text..."):
                docs = [Document(page_content=text_input)]
                st.success("Text processed successfully!")

    # Process documents if they exist
    if 'docs' in locals():
        with st.spinner("Processing documents..."):
            # Split documents
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            all_splits = text_splitter.split_documents(docs)
            
            # Initialize vector store
            st.session_state.vector_store = Chroma(
                collection_name="example_collection",
                embedding_function=embeddings,
                persist_directory="./chroma_langchain_db"
            )
            
            # Add documents to vector store
            st.session_state.vector_store.add_documents(documents=all_splits)
            st.success("Documents processed and indexed!")

    # Question answering section
    if st.session_state.vector_store:
        st.markdown("### ❓ Ask Questions")
        question = st.text_input("Ask a question about the document:")
        
        if question and st.button("Get Answer"):
            with st.spinner("Generating answer..."):
                # Retrieve relevant documents
                retrieved_docs = st.session_state.vector_store.similarity_search(question)
                
                # Generate answer
                prompt = hub.pull("rlm/rag-prompt")
                docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)
                messages = prompt.invoke({"question": question, "context": docs_content})
                response = llm.invoke(messages)
                
                # Display answer
                st.markdown("### Answer:")
                st.markdown(response.content)
                
                # Optionally display sources
                with st.expander("View Sources"):
                    for i, doc in enumerate(retrieved_docs):
                        st.markdown(f"**Source {i+1}:**")
                        st.markdown(doc.page_content)
                        st.markdown("---")

else:
    st.warning("Please enter your Google API key in the sidebar to get started.")
