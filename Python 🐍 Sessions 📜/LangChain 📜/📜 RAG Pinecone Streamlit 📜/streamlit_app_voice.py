import streamlit as st
import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Chroma, Pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from google.generativeai.types.safety_types import HarmBlockThreshold, HarmCategory

# Voice Input/Output
import speech_recognition as sr
from gtts import gTTS
import tempfile
import base64

# Load keys
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")
pinecone_key = os.getenv("PINECONE_API_KEY")
index_name = "langchain-test-index-gemini"

# Streamlit setup
st.set_page_config(page_title="🗣️ Voice Budget Chatbot", layout="centered")
st.title("📊 Indian Budget Chatbot with Voice")
st.markdown("Upload a Budget PDF, speak or type your question, and get spoken answers using Gemini + Pinecone.")

# Upload PDF
uploaded_file = st.file_uploader("📄 Upload a Budget PDF", type="pdf")

if uploaded_file:
    with open("budget_speech.pdf", "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader("budget_speech.pdf")
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(
        model='models/embedding-001',
        google_api_key=gemini_key,
        task_type="retrieval_query"
    )

    os.environ["PINECONE_API_KEY"] = pinecone_key
    vectordb = PineconeVectorStore.from_documents(
        documents=texts,
        embedding=embeddings,
        index_name=index_name
    )

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

    retriever = MultiQueryRetriever.from_llm(
        retriever=vectordb.as_retriever(search_kwargs={"k": 5}),
        llm=chat_model
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=chat_model,
        retriever=retriever,
        return_source_documents=True,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )

    # Voice button
    if st.button("🎙️ Ask by Voice"):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("Listening... Please speak your question clearly.")
            audio = r.listen(source)

        try:
            voice_query = r.recognize_google(audio)
            st.success(f"You asked: {voice_query}")
            response = qa_chain.invoke({"query": voice_query})
            answer = response["result"]
            st.markdown("### 📌 Answer:")
            st.write(answer)

            # Text-to-Speech
            tts = gTTS(answer)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                audio_path = fp.name

            # Embed audio
            with open(audio_path, "rb") as audio_file:
                audio_bytes = audio_file.read()
                b64 = base64.b64encode(audio_bytes).decode()
                st.markdown(
                    f'<audio autoplay controls src="data:audio/mp3;base64,{b64}"></audio>',
                    unsafe_allow_html=True,
                )

            # Show source documents
            with st.expander("🔍 Source Snippets"):
                for i, doc in enumerate(response["source_documents"]):
                    st.markdown(f"**Chunk {i+1}:**")
                    st.write(doc.page_content[:500])

        except sr.UnknownValueError:
            st.error("Sorry, could not understand your voice.")
        except sr.RequestError as e:
            st.error(f"Could not process the request: {e}")

    # Text-based input fallback
    user_query = st.text_input("Or type your question here:")
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
