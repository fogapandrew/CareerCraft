import docx
import os


def word_extractor(filepath):
    """
        This function is used to extract data from a word document.
    """
    doc = docx.Document()
