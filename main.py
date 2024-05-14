# Author: Ricky Bhatti
# Date: May 2024
# Version: 0.1
# Description: Currently, I have no clue what this script will end up doing. So far, the main reason I've started working on thihs script is to be able to merge PDFs together, but I'm not sure what else I'll end up doing with it. We'll see how it goes.
# License: Refer to the LICENSE file. (That'll be released with version 1.0., until then, I'm not sure what the license will be so we'll roll with All Rights Reserved.)

from pypdf import *

pdfs = {}

def parse_pdf(pdf_path):
    pdf = {}
    try: # TODO: Figure out what information we truly want to store for each PDF.
        pdf["reader"] = PdfReader(pdf_path)
        pdf["length"] = len(pdf["reader"])
        pdf["metadata"] = pdf["reader"].get_metadata()
    except Exception as e:
        raise Exception(f"Failed to access PDF at {pdf_path}: {e}")

    return pdf

def main():
    try:
        pdfs["test"] = parse_pdf("test.pdf")
        print(pdfs["test"]["metadata"])
    except Exception as e:
        print(e)
        return

if __name__ == "__main__":
    main()