# Author: Ricky Bhatti
# Date: May 2024
# Version: 0.1
# Description: Currently, I have no clue what this script will end up doing. So far, the main reason I've started working on thihs script is to be able to merge PDFs together, but I'm not sure what else I'll end up doing with it. We'll see how it goes.
# License: Refer to the LICENSE file. (That'll be released with version 1.0., until then, I'm not sure what the license will be so we'll roll with All Rights Reserved.)

# Imports.
import os
from time import sleep
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

def merge_pdfs(pdfs):
    # TODO: Implement this function.
    pass

# write_pdf: This function will write a PDF file to the specified output path.
# Arguments:
#   output_path: The path to the output directory. (Default: Current directory.)
#   pdf_name: The name of the PDF file. (Default: output.pdf)
#   pdf_data: The data to write to the PDF file. (Default: None)
# Returns:
#   None.
# Exceptions:
#   Exception: If the PDF file cannot be written, an exception will be raised.
def write_pdf(output_path = os.getcwd(), pdf_name = "output.pdf", pdf_data = None):
    try: 
        WRITER.write(output_path, pdf_name, pdf_data)
    except Exception as e:
        raise Exception(f"Failed to write PDF to {output_path}: {e}")
    
    return

# clear_screen: This function will clear the screen.
# Arguments:
#   None.
# Returns:
#   None.
# Exceptions:
#   None.
clear_screen = lambda: os.system("cls" if os.name == "nt" else "clear")

# menu: The menu function of the script.
# Arguments:
#   None.
# Returns:
#   None.
# Exceptions:
#   None.
def menu():
    clear_screen()

    # Display the "menu".
    # TODO: Make this an actual menu.
    print("Welcome to the PDF tool!")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Exit")
    
    # Get the user's input.
    user_input = input("Please select an option: ")

    # Handle the user's input.
    while user_input != "5": # NOTE: Quick implementation of the menu. This will be changed later... probably.
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("Invalid option. Please try again.")

        user_input = input("Please select an option: ")

# main: The main function of the script.
# Arguments:
#   None.
# Returns:
#   None.
# Exceptions:
#   None.
def main():
    # region Testing
    # TODO: Remove this testing code.
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

    sleep(5)
    # endregion Testing

    menu()

# If the script is run directly, run the main function.
if __name__ == "__main__":
    main()