import streamlit as st
import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate # Prompt template
from langchain.vectorstores import Chroma,Pinecone   # Store the vectors
from langchain.text_splitter import RecursiveCharacterTextSplitter # Chunks
from langchain.document_loaders import TextLoader,PyPDFLoader  # Load the text
from langchain.chains import VectorDBQA,RetrievalQA, LLMChain # Chains and Retrival ans
from langchain.retrievers.multi_query import MultiQueryRetriever # Multiple Answers
from langchain_google_genai import ChatGoogleGenerativeAI # GenAI model to retrive
from langchain_google_genai import GoogleGenerativeAIEmbeddings # GenAI model to conver words
from langchain_pinecone import PineconeVectorStore
from google.generativeai.types.safety_types import HarmBlockThreshold, HarmCategory

# load keys
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")
pinecone_key = os.getenv("PINECONE_API_KEY")
index_name = "langchain-test-index-gemini"

# Set up Streamlit page
st.set_page_config(page_title="📊 Budget PDF Chatbot", layout="centered")
st.title("📊 Indian Budget Chatbot")
st.markdown("Upload a Budget PDF, ask questions, and get accurate answers using Gemini + Pinecone.")

# Upload PDF
uploaded_file = st.file_uploader("Upload a Budget PDF", type="pdf")

if uploaded_file:
    # Save uploaded file temporarily
    with open("budget_speech.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Load and split PDF
    loader = PyPDFLoader("budget_speech.pdf")
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)

    # Gemini embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model='models/embedding-001',
        google_api_key=gemini_key,
        task_type="retrieval_query"
    )

    # Store in Pinecone
    os.environ["PINECONE_API_KEY"] = pinecone_key
    vectordb = PineconeVectorStore.from_documents(
        documents=texts,
        embedding=embeddings,
        index_name=index_name
    )

    # Gemini LLM
    safety_settings = {
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    }

    chat_model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=gemini_key,
        temperature=0.3,
        safety_settings=safety_settings
    )

    # Prompt
    prompt_template = """
You are an intelligent assistant specialized in analyzing and summarizing Indian Budget speeches and financial documents.

## Instructions:
Use the **context** provided below to answer the **question** clearly and factually. Focus only on the content from the document — do not generate your own opinions or assumptions.

If the answer is **not found in the context**, respond with:
**"The answer is not available in the provided document."**

## Additional Guidelines:
- Avoid political bias or speculation
- Focus on budgetary figures, schemes, reforms, and policy announcements
- Do not infer or hallucinate numbers or statements

---

### Context:
{context}

### Question:
{question}

### Answer:
"""
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    # Retriever
    retriever = MultiQueryRetriever.from_llm(
        retriever=vectordb.as_retriever(search_kwargs={"k": 5}),
        llm=chat_model
    )

    # QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=chat_model,
        retriever=retriever,
        return_source_documents=True,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )

    # Query input
    user_query = st.text_input("Ask a question about the Budget:", key="query")

    if user_query:
        with st.spinner("Fetching answer..."):
            response = qa_chain.invoke({"query": user_query})
            st.markdown("### 📌 Answer:")
            st.write(response["result"])

            with st.expander("🔍 Source Snippets"):
                for i, doc in enumerate(response["source_documents"]):
                    st.markdown(f"**Chunk {i+1}:**")
                    st.write(doc.page_content[:500])

else:
    st.info("Please upload a Budget PDF to begin.")
