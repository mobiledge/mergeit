import os
import sys
from PyPDF2 import PdfMerger

def merge_pdfs(folder_path):
    # Create a PdfMerger object
    merger = PdfMerger()

    # Get all PDF files in the folder
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    if not pdf_files:
        print("No PDF files found in the specified folder.")
        return

    # Sort the PDF files alphabetically
    pdf_files.sort()

    # Merge the PDFs
    for pdf in pdf_files:
        merger.append(os.path.join(folder_path, pdf))

    # Write the merged PDF to a file
    output_path = os.path.join(folder_path, 'merged_output.pdf')
    merger.write(output_path)
    merger.close()

    print(f"Merged PDF saved as: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print("Error: The provided path is not a valid directory.")
        sys.exit(1)

    merge_pdfs(folder_path)
