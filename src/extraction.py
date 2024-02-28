import utilities
import os

DATA_DIR = utilities.get_data_directory_path()


def extraction_cv(filepath):
    """
        This function is used to extract from the csv or word document.
    """
    if filepath.lower().endswith('.docx'):
        # this return the extracted data in type string.
        return utilities.word_extractor(filepath)
    else:
        return utilities.pdf_extractor(filepath)


nameofcv = input("Enter name of CV (PDF at the end): ")

filepath = os.path.join(DATA_DIR, "cvs", nameofcv)

print(filepath)
extracted_text = extraction_cv(filepath)

print("here : ", extracted_text)
