import fitz  # PyMuPDF
import io
import os

def extract_formulas_from_bytes(pdf_bytes, output_folder="output_formulas"):
    """
    Extracts lines of text that look like formulas/equations and saves them to a text file.
    """
    if not pdf_bytes:
        print("[formulas] No data to process.")
        return

    os.makedirs(output_folder, exist_ok=True)
    print("[formulas] Starting formula extraction...")

    try:
        pdf_stream = io.BytesIO(pdf_bytes)
        doc = fitz.open(stream=pdf_stream, filetype="pdf")
        
        extracted_formulas = []
        
        # Heuristic keywords from your notebook
        math_indicators = ["(", ")", "sqrt", "/", "Q", "K", "V", "sin", "cos", "theta"]

        for page_num, page in enumerate(doc):
            text = page.get_text()
            lines = text.split("\n")
            
            for line in lines:
                # Basic heuristic: Line must have '=' AND at least one math symbol
                if "=" in line and any(x in line for x in math_indicators):
                    clean_line = line.strip()
                    extracted_formulas.append(f"Page {page_num + 1}: {clean_line}")

        # Save to file
        output_path = os.path.join(output_folder, "extracted_formulas.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            for item in extracted_formulas:
                f.write(item + "\n")

        print(f"[formulas] Extracted {len(extracted_formulas)} potential formulas to '{output_path}'.")
        return extracted_formulas

    except Exception as e:
        print(f"[formulas] Error extracting formulas: {e}")
        return []