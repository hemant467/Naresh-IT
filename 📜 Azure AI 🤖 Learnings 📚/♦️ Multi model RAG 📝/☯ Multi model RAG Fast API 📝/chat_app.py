import os
import dotenv
import google.generativeai as genai
from pinecone import Pinecone

# Load environment variables
dotenv.load_dotenv()

# --- Configuration ---
PINECONE_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
GOOGLE_API_KEY = os.getenv("Gemini_Api")

# --- Initialization ---
# 1. Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# 2. Configure Pinecone
pc = Pinecone(api_key=PINECONE_KEY)
index = pc.Index(PINECONE_INDEX_NAME)

def get_embedding(text):
    """
    Generates embedding for the user's query.
    """
    response = genai.embed_content(
        model="models/embedding-001",
        content=text,
        task_type="retrieval_query"
    )
    return response['embedding']

def retrieve_context(query_vector, top_k=5):
    """
    Searches Pinecone for the most similar chunks.
    """
    results = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )
    
    # Extract just the text from the metadata
    contexts = []
    for match in results['matches']:
        if 'text' in match['metadata']:
            contexts.append(match['metadata']['text'])
    
    return contexts

def generate_answer(query, context_list):
    """
    Sends the query and retrieved context to Gemini Pro for an answer.
    """
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # Join the context chunks into a single string
    context_text = "\n\n---\n\n".join(context_list)
    
    prompt = f"""
    You are a helpful AI assistant. Use the following context to answer the user's question.
    If the answer is not in the context, say "I don't know based on the provided document."

    Context:
    {context_text}

    Question: 
    {query}

    Answer:
    """
    
    response = model.generate_content(prompt)
    return response.text

def start_chat():
    print("=== Document Chatbot (Type 'exit' to quit) ===")
    
    while True:
        query = input("\nUser: ")
        if query.lower() in ["exit", "quit"]:
            break
            
        try:
            # 1. Embed Query
            query_vector = get_embedding(query)
            
            # 2. Retrieve Context
            contexts = retrieve_context(query_vector)
            
            if not contexts:
                print("Bot: No relevant information found in the document.")
                continue
                
            # 3. Generate Answer
            answer = generate_answer(query, contexts)
            
            print(f"\nBot: {answer}")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start_chat()