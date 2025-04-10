import pdfplumber
import json
import re
import os
import warnings
import logging
from typing import List, Dict

# Suppress all warnings
warnings.filterwarnings('ignore')
logging.getLogger('pdfminer').setLevel(logging.ERROR)

def extract_data_from_pdf(pdf_path: str) -> List[Dict[str, str]]:
    data = []
    headers = ["division", "district", "upazilla", "union_parishad"]
    
    try:
        # Verify if file is actually a PDF
        with open(pdf_path, 'rb') as file:
            header = file.read(4)
            if header != b'%PDF':
                raise ValueError("The file is not a valid PDF document")
        
        # Configure PDF reader with custom settings - removed invalid parameter
        with pdfplumber.open(pdf_path) as pdf:
            if len(pdf.pages) == 0:
                raise ValueError("The PDF file is empty")
                
            for page in pdf.pages:
                text = page.extract_text(x_tolerance=3, y_tolerance=3)
                if not text:
                    continue
                
                # Process text line by line
                lines = [line for line in text.split('\n') if line.strip()]
                
                for line in lines:
                    if any(h.lower() in line.lower() for h in headers):
                        continue
                    
                    columns = clean_and_split_line(line)
                    if len(columns) >= 4:
                        union_parishad = ' '.join(columns[3:])
                        entry = {
                            headers[0]: columns[0],
                            headers[1]: columns[1],
                            headers[2]: columns[2],
                            headers[3]: union_parishad
                        }
                        data.append(entry)
    except FileNotFoundError:
        print(f"Could not open the file: {pdf_path}")
    except ValueError as ve:
        print(f"PDF Error: {str(ve)}")
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
    return data

def main():
    pdf_path = r"c:\Users\MOB\Downloads\python\union_parishads.pdf"
    output_json_path = r"c:\Users\MOB\Downloads\python\union_parishads.json"
    
    try:
        # Check file size
        if os.path.exists(pdf_path):
            if os.path.getsize(pdf_path) == 0:
                print("Error: The PDF file is empty")
                return
        else:
            print("Error: PDF file not found")
            print("Expected location:", pdf_path)
            print("Please ensure you have placed a valid PDF file at this location")
            return
            
        # Extract data from the PDF
        print("Starting PDF conversion...")
        extracted_data = extract_data_from_pdf(pdf_path)
        
        if not extracted_data:
            print("No data extracted from the PDF.")
            print("Please ensure the PDF contains the expected data format.")
            return
        
        # Save the extracted data to a JSON file
        save_to_json(extracted_data, output_json_path)
        print(f"Data successfully converted and saved to {output_json_path}")
        
        # Print a sample of the extracted data
        print("\nSample of extracted data (first 5 entries):")
        for item in extracted_data[:5]:
            print(json.dumps(item, indent=2, ensure_ascii=False))
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please ensure the PDF file is not corrupted and is readable.")

# Function to clean and split text into columns
def clean_and_split_line(line: str) -> List[str]:
    # Replace multiple spaces/tabs with a single delimiter and split
    cleaned_line = re.sub(r'\s+', ' ', line.strip())
    return cleaned_line.split(' ')

# Function to save data as JSON
def save_to_json(data: List[Dict[str, str]], output_file: str):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# Main execution
def main():
    # Use absolute paths
    pdf_path = r"c:\Users\MOB\Downloads\python\union_parishads.pdf"
    output_json_path = r"c:\Users\MOB\Downloads\python\union_parishads.json"
    
    try:
        # Check if PDF file exists
        if not os.path.exists(pdf_path):
            print(f"Error: PDF file not found at {pdf_path}")
            print("Please place your PDF file in the correct location.")
            return
            
        # Extract data from the PDF
        print("Starting PDF conversion...")
        extracted_data = extract_data_from_pdf(pdf_path)
        
        if not extracted_data:
            print("No data extracted from the PDF.")
            print("Please ensure the PDF contains the expected data format.")
            return
        
        # Save the extracted data to a JSON file
        save_to_json(extracted_data, output_json_path)
        print(f"Data successfully converted and saved to {output_json_path}")
        
        # Print a sample of the extracted data
        print("\nSample of extracted data (first 5 entries):")
        for item in extracted_data[:5]:
            print(json.dumps(item, indent=2, ensure_ascii=False))
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please ensure the PDF file is not corrupted and is readable.")

if __name__ == "__main__":
    main()