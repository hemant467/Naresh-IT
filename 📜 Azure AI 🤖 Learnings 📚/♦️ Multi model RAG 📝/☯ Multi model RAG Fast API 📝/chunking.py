from PyPDF2 import PdfReader
# ---------------------------------------------------------
# FIX: Use the underscore (_) not dot (.) for this library
# ---------------------------------------------------------
from langchain_text_splitters import RecursiveCharacterTextSplitter
import io

def extract_text_and_chunk(pdf_bytes, chunk_size=1000, overlap=100):
    """
    Extracts text from PDF bytes and splits it using RecursiveCharacterTextSplitter.
    """
    if not pdf_bytes:
        print("[chunking] No data to process.")
        return []

    print("[chunking] Extracting text...")
    try:
        pdf_stream = io.BytesIO(pdf_bytes)
        reader = PdfReader(pdf_stream)
        
        full_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"

        print(f"[chunking] Extracted {len(full_text)} characters. Chunking with RecursiveCharacterTextSplitter...")
        
        # Initialize the splitter
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap,
            length_function=len,
            is_separator_regex=False,
        )
        
        # Create chunks
        chunks = text_splitter.split_text(full_text)
            
        print(f"[chunking] Created {len(chunks)} chunks.")
        return chunks
    except Exception as e:
        print(f"[chunking] Error processing text: {e}")
        return []