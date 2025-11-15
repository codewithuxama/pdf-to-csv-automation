import PyPDF2
import csv
import re

def pdf_to_csv(pdf_path, csv_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        extracted_text = ""

        for page in reader.pages:
            extracted_text += page.extract_text()

    # Clean and split into lines
    lines = extracted_text.split("\n")

    # Export to CSV
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for line in lines:
            cleaned = re.split(r'\s{2,}', line)
            writer.writerow(cleaned)

    print(f"CSV created: {csv_path}")

# Example usage
pdf_to_csv("input.pdf", "output.csv")
