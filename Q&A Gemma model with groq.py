import streamlit as st
import os
import time
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load environment variables
load_dotenv()

# Set API Keys
groq_api_key = os.getenv('GROQ_API_KEY')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Streamlit UI
st.title("Gemma Model Document Q&A chatbot")

# Load LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="Llama3-8b-8192"
)

# Prompt Template
prompt = ChatPromptTemplate.from_template("""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question.

<context>
{context}
</context>

Question: {input}
""")

# Vector Embedding Function
def vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        st.session_state.loader = PyPDFDirectoryLoader("./us_census")  # Load PDF folder
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:20])
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)
        st.success("Vector Store DB is Ready!")
    else:
        st.info("Vector Store DB already initialized.")

# Button to generate vector embeddings
if st.button("Create Document Embeddings"):
    vector_embedding()

# Text input
prompt1 = st.text_input("Enter Your Question From Documents")

# Handle query
if prompt1:
    if "vectors" not in st.session_state:
        st.warning("Please click on 'Create Document Embeddings' first to load the documents.")
    else:
        document_chain = create_stuff_documents_chain(llm, prompt)
        retriever = st.session_state.vectors.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)

        start = time.process_time()
        response = retrieval_chain.invoke({'input': prompt1})
        end = time.process_time()

        st.write("### Answer:")
        st.write(response['answer'])
        st.caption(f"⏱️ Response Time: {round(end - start, 2)} seconds")

        with st.expander("🔍 Document Similarity Search"):
            for i, doc in enumerate(response["context"]):
                st.markdown(f"**Chunk {i + 1}:**")
                st.write(doc.page_content)
                st.write("---")
