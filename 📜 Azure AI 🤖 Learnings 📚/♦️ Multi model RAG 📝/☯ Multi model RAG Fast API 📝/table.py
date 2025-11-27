import camelot
import tempfile
import os
import pandas as pd

def extract_tables_from_bytes(pdf_bytes, output_folder="output_tables"):
    """
    Extracts tables and returns them as a list of Markdown strings for embedding.
    """
    if not pdf_bytes:
        print("[table] No data to process.")
        return []

    os.makedirs(output_folder, exist_ok=True)
    print("[table] Starting table extraction...")
    
    table_texts = [] # List to store string representation of tables
    temp_pdf_path = None
    
    try:
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
            tmp.write(pdf_bytes)
            temp_pdf_path = tmp.name

        # Extract tables
        tables = camelot.read_pdf(temp_pdf_path, pages="all")
        print(f"[table] Found {len(tables)} tables.")

        for i, tbl in enumerate(tables):
            # 1. Save CSV (Keep existing logic)
            output_path = os.path.join(output_folder, f"table_{i+1}.csv")
            tbl.to_csv(output_path)
            
            # 2. Convert to Markdown for LLM (New Logic)
            # We add a header so the LLM knows this is a table
            try:
                df = tbl.df
                markdown_text = f"Table {i+1} Data:\n" + df.to_markdown(index=False)
                table_texts.append(markdown_text)
            except Exception as e:
                # Fallback if markdown conversion fails
                table_texts.append(f"Table {i+1} Data:\n" + df.to_string())

            print(f"[table] Processed Table {i+1}")
            
        return table_texts

    except Exception as e:
        print(f"[table] Error extracting tables: {e}")
        return []
    finally:
        if temp_pdf_path and os.path.exists(temp_pdf_path):
            os.remove(temp_pdf_path)