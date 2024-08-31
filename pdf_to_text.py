import fitz  

def pdf_to_text(pdf_path, output_txt_path):
    try:
        # Open the PDF file
        doc = fitz.open(pdf_path)
        
        # Initialize a variable to store all the extracted text
        text = ""
        
        # Iterate through each page and extract text
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)  # Load each page
            text += page.get_text()  # Extract text from the page
            
        # Save the extracted text to a file
        with open(output_txt_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print(f"Text extracted and saved to {output_txt_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
pdf_to_text("Flash Distillation.pdf", "output.txt")
