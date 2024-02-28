import docx
import os
import PyPDF2


def get_data_directory_path():
    """
        function is used to get path
    """
    ROOT_DIR = os.getcwd()
    # This is to extract the patent directory from the ful path(ETLSystem)
    ROOT_DIR = os.path.dirname(ROOT_DIR)
    DATA_DIR = os.path.join(ROOT_DIR, "rawdata")

    return DATA_DIR


def word_extractor(filepath):
    """
        function is used to extract data from a word document
    """
    doc = docx.Document(filepath)  # Reading in the file using Document method
    extracted_text = []  # an array that would hold the extracted file
    for paragraph in doc.paragraphs:
        # loop through each paragraph in the word doc and extracting the text.
        extracted_text.append(paragraph.text)

    return "\n".join(extracted_text)


def pdf_extractor(filepath):
    """
        function is used to extract data from a word pdf document
    """
    with open(filepath, 'rb') as pdf_file:  # reading in the pdf file
        # using a pdfreader to read in the file as a pdf
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        extracted_text = ""  # empty string that holds the extracted data

        # loops that loop over each page of the pdf and extract text form it and add its to the empty string
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            extracted_text += page_text

    return extracted_text
