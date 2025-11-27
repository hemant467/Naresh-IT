import os
import time
from pinecone import Pinecone, ServerlessSpec

def init_pinecone(api_key, index_name, dimension=768):
    # ... (Keep the init_pinecone function EXACTLY as it was in the previous step) ...
    # ... (Copy the init_pinecone code I gave you previously) ...
    if not api_key or not index_name:
        print("[vector_store] Error: Missing Pinecone credentials.")
        return None

    print(f"[vector_store] Connecting to Pinecone...")
    pc = Pinecone(api_key=api_key)
    existing_indexes = [i["name"] for i in pc.list_indexes()]
    
    if index_name not in existing_indexes:
        print(f"[vector_store] Creating new index '{index_name}' on AWS (us-east-1)...")
        try:
            pc.create_index(
                name=index_name,
                dimension=dimension,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )
            time.sleep(10)
        except Exception as e:
            print(f"[vector_store] Failed to create index: {e}")
            return None
    return pc.Index(index_name)

def upsert_vectors(index, content_list, embedding_list, metadata_list):
    """
    Flexible upsert function that handles text, tables, and formulas.
    """
    if not index:
        return

    if len(content_list) != len(embedding_list):
        print("[vector_store] Error: Mismatch between content and embeddings count.")
        return

    print(f"[vector_store] Preparing to upsert {len(content_list)} items...")
    
    vectors_to_upsert = []
    
    for i, (text, vector, meta) in enumerate(zip(content_list, embedding_list, metadata_list)):
        vector_id = f"{meta['type']}_{i}_{int(time.time())}" # Unique ID e.g., table_0_12345
        
        # Ensure text matches metadata
        meta["text"] = text[:30000] # Safety limit
        
        vectors_to_upsert.append({
            "id": vector_id, 
            "values": vector, 
            "metadata": meta
        })

    # Batch upsert
    batch_size = 100
    for i in range(0, len(vectors_to_upsert), batch_size):
        batch = vectors_to_upsert[i : i + batch_size]
        try:
            index.upsert(vectors=batch)
            print(f"[vector_store] Upserted batch {i} to {i+len(batch)}")
        except Exception as e:
            print(f"[vector_store] Error upserting batch: {e}")

    print("[vector_store] Upload complete.")