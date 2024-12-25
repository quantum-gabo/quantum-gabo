#!/usr/bin/env python3

from PyPDF2 import PdfReader

def count_characters_in_pdf(pdf_file):
    try:
        pdf_reader = PdfReader(pdf_file)
        total_characters = 0

        for page in pdf_reader.pages:
            total_characters += len(page.extract_text())

        return total_characters

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    pdf_file_path = "./cover_letter.pdf"  # Replace with the path to your PDF file
    character_count = count_characters_in_pdf(pdf_file_path)

    if isinstance(character_count, int):
        print(f"Total characters in the PDF: {character_count}")
    else:
        print(f"Error: {character_count}")

