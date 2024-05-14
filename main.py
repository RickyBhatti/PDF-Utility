# Author: Ricky Bhatti
# Date: May 2024
# Version: 0.1
# Description: Currently, I have no clue what this script will end up doing. So far, the main reason I've started working on thihs script is to be able to merge PDFs together, but I'm not sure what else I'll end up doing with it. We'll see how it goes.
# License: Refer to the LICENSE file. (That'll be released with version 1.0., until then, I'm not sure what the license will be so we'll roll with All Rights Reserved.)

# Imports.
from pypdf import *

# Constants.
WRITER = PdfWriter()

# Global variables.
pdfs = {}

# parse_pdf: This function will parse a PDF file and return a dictionary containing the PDF's reader object, length, and metadata.
# Arguments:
#   pdf_path: The path to the PDF file.
# Returns:
#   pdf: A dictionary containing the PDF's reader object, length, and metadata.
# Exceptions:
#   Exception: If the PDF file cannot be accessed, an exception will be raised.
def parse_pdf(pdf_path):
    pdf = {}
    try: # TODO: Figure out what information we truly want to store for each PDF.
        pdf["reader"] = PdfReader(pdf_path)
        pdf["length"] = pdf["reader"].get_num_pages()
        pdf["metadata"] = pdf["reader"].metadata
    except Exception as e:
        raise Exception(f"Failed to access PDF at {pdf_path}: {e}")

    return pdf

# menu: The menu function of the script.
# Arguments:
#   None.
# Returns:
#   None.
# Exceptions:
#   None.
def menu():
    pass

# main: The main function of the script.
# Arguments:
#   None.
# Returns:
#   None.
# Exceptions:
#   None.
def main():
    try:
        pdfs["test"] = parse_pdf("test2.pdf")
        print(pdfs["test"]["metadata"])
    except Exception as e:
        print(e)
        return

    print('-' * 50)
    test_reader = PdfReader("test2.pdf")
    print(test_reader.metadata)
    print('-' * 50)
    print(test_reader.get_num_pages())
    print('-' * 50)
    print(test_reader.pages[0].extract_text()[0:100]) # Extract the text from the first page of the PDF, and print the first 100 characters.

# If the script is run directly, run the main function.
if __name__ == "__main__":
    main()