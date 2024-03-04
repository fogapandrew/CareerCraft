import utilities
import os

DATA_DIR = utilities.get_data_directory_path()


def extraction_data(filepath):
    """
        This function is used to extract from the csv or word document.
    """
    if filepath.lower().endswith('.docx'):
        # this return the extracted data in type string.
        return utilities.word_extractor(filepath)
    else:
        return utilities.pdf_extractor(filepath)


nameofcv = input("Enter name of CV (PDF at the end): ")

filepathforcv = os.path.join(DATA_DIR, "cvs", "FogapCV.pdf")

filepathforjobrequirements = os.path.join(DATA_DIR, "otherdocs", "data.docx")

extracted_cv = extraction_data(filepathforcv)

extracted_jobrequirements = extraction_data(filepathforjobrequirements)
