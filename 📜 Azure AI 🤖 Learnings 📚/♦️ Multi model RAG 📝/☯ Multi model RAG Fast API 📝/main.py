import os
import dotenv

dotenv.load_dotenv()

import read_data
import img
import table
import formula
import chunking
import embedding
import vector_store

# --- Configuration ---
CONN_STR = os.getenv("connection_url")
CONTAINER = os.getenv("container_name")
BLOB_NAME = os.getenv("blob_name")
GOOGLE_API_KEY = os.getenv('Gemini_Api')
PINECONE_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX_NAME")

def run_pipeline():
    print("=== Multi-RAG Pipeline Started (Text + Tables + Formulas + Images) ===")
    
    # 1. Data Read
    pdf_bytes = read_data.download_blob_data(CONN_STR, CONTAINER, BLOB_NAME)
    
    if pdf_bytes:
        # --- EXTRACT EVERYTHING ---
        
        # A. Images (Extract -> Caption)
        image_paths = img.extract_images_from_bytes(pdf_bytes, output_folder="output_images")
        image_captions = []
        if image_paths and GOOGLE_API_KEY:
            image_captions, valid_image_paths = img.generate_image_captions(image_paths, GOOGLE_API_KEY)
        
        # B. Tables (Get Markdown Strings)
        table_strings = table.extract_tables_from_bytes(pdf_bytes, output_folder="output_tables")
        
        # C. Formulas (Get Formula Strings)
        formula_strings = formula.extract_formulas_from_bytes(pdf_bytes, output_folder="output_formulas")
        
        # D. Text Chunks
        text_chunks = chunking.extract_text_and_chunk(pdf_bytes, chunk_size=1000, overlap=200)

        # --- PREPARE MULTI-MODAL DATA FOR EMBEDDING ---
        all_content = []
        all_metadata = []

        # 1. Add Text
        for t in text_chunks:
            all_content.append(t)
            all_metadata.append({"type": "text", "source": BLOB_NAME})
            
        # 2. Add Tables
        for t in table_strings:
            all_content.append(t)
            all_metadata.append({"type": "table", "source": BLOB_NAME})

        # 3. Add Formulas
        for f in formula_strings:
            all_content.append(f"Mathematical Formula: {f}")
            all_metadata.append({"type": "formula", "source": BLOB_NAME})

        # 4. Add Images
        for i, caption in enumerate(image_captions):
            all_content.append(caption)
            # We store the image path in metadata so a UI could potentially display it later
            all_metadata.append({
                "type": "image", 
                "source": BLOB_NAME, 
                "image_path": valid_image_paths[i]
            })

        print(f"\n[Pipeline] Total items to embed: {len(all_content)}")
        print(f"   - Text Chunks: {len(text_chunks)}")
        print(f"   - Tables: {len(table_strings)}")
        print(f"   - Formulas: {len(formula_strings)}")
        print(f"   - Images: {len(image_captions)}")

        # --- EMBED & STORE ---
        if all_content and GOOGLE_API_KEY:
            vectors = embedding.generate_embeddings(all_content, api_key=GOOGLE_API_KEY)
            
            if vectors:
                print("\n[Pipeline] Initializing Vector Database...")
                index = vector_store.init_pinecone(api_key=PINECONE_KEY, index_name=PINECONE_INDEX)
                
                if index:
                    vector_store.upsert_vectors(index, all_content, vectors, all_metadata)

        print("\n=== Pipeline Completed Successfully ===")
    else:
        print("Pipeline aborted: Failed to download data.")

if __name__ == "__main__":
    run_pipeline()