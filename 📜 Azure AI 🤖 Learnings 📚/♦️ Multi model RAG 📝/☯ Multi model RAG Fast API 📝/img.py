import fitz  # PyMuPDF
import io
import os
import time
import PIL.Image
import google.generativeai as genai

def extract_images_from_bytes(pdf_bytes, output_folder="output_images"):
    """
    Extracts images from PDF bytes, saves them, and returns a list of their file paths.
    """
    if not pdf_bytes:
        print("[img] No data to process.")
        return []

    os.makedirs(output_folder, exist_ok=True)
    print("[img] Starting image extraction...")
    
    saved_image_paths = []
    
    try:
        pdf_stream = io.BytesIO(pdf_bytes)
        doc = fitz.open(stream=pdf_stream, filetype="pdf")
        
        image_count = 0
        
        for page_index, page in enumerate(doc):
            images = page.get_images(full=True)
            for img_index, img in enumerate(images):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                
                # Filter out tiny images (logos, lines) < 5KB to save API costs
                if len(image_bytes) < 5120: 
                    continue
                
                image_filename = f"page{page_index+1}_img{img_index+1}.{image_ext}"
                image_path = os.path.join(output_folder, image_filename)
                
                with open(image_path, "wb") as f:
                    f.write(image_bytes)
                
                saved_image_paths.append(image_path)
                image_count += 1
        
        print(f"[img] Extracted {image_count} meaningful images to '{output_folder}'.")
        return saved_image_paths

    except Exception as e:
        print(f"[img] Error extracting images: {e}")
        return []

def generate_image_captions(image_paths, api_key):
    """
    Uses Gemini 1.5 Flash to generate descriptive text for each image.
    """
    if not image_paths:
        return [], []

    print(f"[img] Generating captions for {len(image_paths)} images using Gemini...")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    captions = []
    valid_paths = [] # Keep track of which images successfully got captions

    for img_path in image_paths:
        try:
            image = PIL.Image.open(img_path)
            
            # Prompt for technical document images
            prompt = "Analyze this image from a technical document. Describe the diagram, chart, or visual content in detail so that the information can be indexed for search."
            
            response = model.generate_content([prompt, image])
            
            # Create a formatted string for the RAG system
            description = f"Image Description (Source: {os.path.basename(img_path)}):\n{response.text}"
            
            captions.append(description)
            valid_paths.append(img_path)
            
            print(f"[img] Captioned: {os.path.basename(img_path)}")
            
            # Rate limiting (Gemini Free tier has limits)
            time.sleep(2) 
            
        except Exception as e:
            print(f"[img] Failed to caption {img_path}: {e}")

    return captions, valid_paths