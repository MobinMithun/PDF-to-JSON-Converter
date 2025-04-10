# PDF Data Extractor to JSON

This Python script extracts data from a PDF file containing information about divisions, districts, upazilas, and union parishads, then converts the extracted data into a structured JSON format.

---

## Requirements

- **Python 3.x**
- **Libraries**:
  - `pdfplumber`
  - `json`
  - `re`
  - `os`
  - `warnings`
  - `logging`

You can install the required dependencies using pip:

---

## Functionality

The script performs the following tasks:

1. **Extract Data from PDF**: It opens the provided PDF, reads its content, and extracts lines containing the relevant information (division, district, upazila, and union parishad).
2. **Clean and Split Data**: It processes each line by cleaning extra spaces and splitting it into the required columns.
3. **Save Data to JSON**: The script saves the extracted data in a JSON file at the specified location.

---

## Data Format

The script looks for the following columns in the PDF data:

- **Division**
- **District**
- **Upazila**
- **Union Parishad**

Example of Extracted Data Format:
```json
[
  {
    "division": "Dhaka",
    "district": "Dhaka",
    "upazilla": "Gulshan",
    "union_parishad": "Union Parishad 1"
  },
  ...
]
```

---------------------------------------------

## Instructions
1. Ensure Python and Required Libraries Are Installed
If you haven't already, install the necessary libraries by running:
