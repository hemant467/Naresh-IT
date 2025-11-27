from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import chat_app  # Imports logic from your existing chat_app.py

# Initialize App
app = FastAPI(
    title="Multi-RAG Chatbot API",
    description="API for chatting with PDF documents (Text, Tables, Images, Formulas)",
    version="1.0"
)

# --- Request/Response Models ---
class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: str
    sources: list[str] = []

# --- Endpoints ---
@app.get("/")
def health_check():
    return {"status": "active", "service": "RAG API"}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Accepts a query, searches the vector database, and returns an answer.
    """
    try:
        # 1. Embed Query (using chat_app logic)
        query_vector = chat_app.get_embedding(request.query)
        
        # 2. Retrieve Context (using chat_app logic)
        # Note: We rely on chat_app to get the text list
        contexts = chat_app.retrieve_context(query_vector)
        
        if not contexts:
            return ChatResponse(
                answer="I couldn't find relevant information in the document based on your query.",
                sources=[]
            )
            
        # 3. Generate Answer (using chat_app logic)
        answer = chat_app.generate_answer(request.query, contexts)
        
        # 4. Return Response
        return ChatResponse(
            answer=answer,
            sources=contexts  # We return the context snippets as "sources" for transparency
        )

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# --- Run Server ---
if __name__ == "__main__":
    print("Starting API Server...")
    print("Swagger UI available at: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)

