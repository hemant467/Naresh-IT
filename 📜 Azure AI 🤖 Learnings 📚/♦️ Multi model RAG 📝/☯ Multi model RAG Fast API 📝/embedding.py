import google.generativeai as genai
import time

def generate_embeddings(chunks, api_key, model_name="models/embedding-001"):
    """
    Generates embeddings for text chunks using Google Gemini API.
    """
    if not chunks:
        print("[embedding] No chunks to embed.")
        return []

    if not api_key:
        print("[embedding] Error: Missing Google API Key.")
        return []

    print(f"[embedding] Configuring Gemini...")
    try:
        genai.configure(api_key=api_key)

        embeddings = []
        batch_size = 10  # Process in small batches
        
        print(f"[embedding] Generating embeddings for {len(chunks)} chunks...")

        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]
            
            # Use embed_content for batch embedding
            response = genai.embed_content(
                model=model_name,
                content=batch,
                task_type="retrieval_document"
            )
            
            if 'embedding' in response:
                embeddings.extend(response['embedding'])
            
            # Brief pause to respect rate limits
            time.sleep(0.5) 
            
        print(f"[embedding] Successfully generated {len(embeddings)} vectors.")
        return embeddings

    except Exception as e:
        print(f"[embedding] Error generating embeddings: {e}")
        return []