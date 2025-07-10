import streamlit as st
import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from google.generativeai.types.safety_types import HarmBlockThreshold, HarmCategory

# Voice & Audio
import speech_recognition as sr
from gtts import gTTS
import tempfile
import base64

# ✅ Translator
from deep_translator import GoogleTranslator

# Load API keys
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")
pinecone_key = os.getenv("PINECONE_API_KEY")
index_name = "langchain-test-index-gemini"

# Streamlit UI setup
st.set_page_config(page_title="🗣️ Multilingual Budget Chatbot", layout="centered")
st.title("📊 Indian Budget Voice Chatbot (with Translation)")
st.markdown("Upload a Budget PDF, speak/type your question in your language, and hear the answer.")

# Language selection
language_codes = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Bengali": "bn",
    "Punjabi": "pa",
    "Malayalam": "ml"
}
selected_language = st.selectbox("🌐 Choose your language:", list(language_codes.keys()))
lang_code = language_codes[selected_language]

# PDF Upload
uploaded_file = st.file_uploader("📄 Upload a Budget PDF", type="pdf")

if uploaded_file:
    with open("budget_speech.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Load & split PDF
    loader = PyPDFLoader("budget_speech.pdf")
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = splitter.split_documents(documents)

    # Gemini embeddings
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

    # Prompt Template
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

    # 🎙️ Voice Input
    if st.button("🎤 Speak Your Question"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("🎙️ Listening... Speak clearly.")
            audio = recognizer.listen(source)

        try:
            user_voice = recognizer.recognize_google(audio, language=lang_code + "-IN")
            st.success(f"🗣️ You asked: {user_voice}")

            # Translate to English
            translated_query = GoogleTranslator(source=lang_code, target="en").translate(user_voice)

            # Get Gemini Answer
            response = qa_chain.invoke({"query": translated_query})
            answer_en = response["result"]

            # Translate back
            translated_answer = GoogleTranslator(source="en", target=lang_code).translate(answer_en)
            st.markdown("### 📌 Answer (Translated):")
            st.write(translated_answer)

            # 🔊 Speak the answer
            tts = gTTS(translated_answer, lang=lang_code)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                audio_path = fp.name

            with open(audio_path, "rb") as af:
                audio_bytes = af.read()
                b64 = base64.b64encode(audio_bytes).decode()
                st.markdown(f'<audio autoplay controls src="data:audio/mp3;base64,{b64}"></audio>', unsafe_allow_html=True)

            # Show Sources
            with st.expander("📚 Source Snippets"):
                for i, doc in enumerate(response["source_documents"]):
                    st.markdown(f"**Chunk {i+1}:**")
                    st.write(doc.page_content[:500])

        except sr.UnknownValueError:
            st.error("Could not understand your voice.")
        except sr.RequestError as e:
            st.error(f"Voice processing error: {e}")

    # 📝 Text Input
    user_query = st.text_input("Or type your question:")
    if user_query:
        with st.spinner("Translating and answering..."):
            translated_q = GoogleTranslator(source=lang_code, target="en").translate(user_query)
            response = qa_chain.invoke({"query": translated_q})
            translated_a = GoogleTranslator(source="en", target=lang_code).translate(response["result"])

            st.markdown("### 📌 Answer (Translated):")
            st.write(translated_a)

            with st.expander("📚 Source Snippets"):
                for i, doc in enumerate(response["source_documents"]):
                    st.markdown(f"**Chunk {i+1}:**")
                    st.write(doc.page_content[:500])
else:
    st.info("📁 Please upload a Budget PDF to begin.")
