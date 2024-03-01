from extraction import extracted_jobrequirements, extracted_cv
import utilities
import spacy
import re


# getting all email of users before transforming it.
all_email = utilities.find_emails(extracted_cv)

# Class for transformation(removing personal information) of both cv and job requirements.


class Transformation:
    """
        This class has methods that masked personal information of the cv and job description.
        The masking_on_data method using regex and spacy to find and masked personal information of data.
        It returns the masked data, the number of masked data and the different data that was masked.
    """

    def __init__(self, extraction_data):
        self.extraction_data = extraction_data

    def masking_on_data(self):
        data = self.extraction_data
        data = utilities.mask_personal_information_2(data)
        # data = utilities.clean_phone_number(data)

        # Load the pre-trained statistical model
        nlp = spacy.load("en_core_web_sm")
        # Process the text using spaCy
        doc = nlp(data)

        # List to store all the proper-nouns for human names
        pii = []

        mob_regex = r"\+?\d{1,4}[-\s\.]?\(?\d{1,4}\)?[-\s\.]?\d{1,10}[-\s\.]?\d{1,10}[-\s\.]?\d{1,10}"

        email_regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        # Common non-human names that we want to filter out
        excluded_names = {"Coursera", "Git", "Github", "Linkedln", "Python"}

        for token in doc:
            if token.pos_ == 'PROPN':
                # Check if it's a person's name or a country name based on NER
                if token.ent_type_ in ['PERSON', 'GPE'] and token.text.lower() not in map(str.lower, excluded_names):
                    pii.append(token.text)
                    # Replace the name with a mask (e.g., "MASKED")
                    data = re.sub(r'\b' + re.escape(token.text) +
                                  r'\b', "*****", data, flags=re.I)
            elif re.search(mob_regex, str(token), re.IGNORECASE):
                pii.append(token.text)
                data = re.sub(re.escape(token.text), "*****", data, flags=re.I)
            elif re.search(email_regex, token.text, re.IGNORECASE):
                pii.append(token.text)
                data = re.sub(re.escape(token.text), "*****", data, flags=re.I)

        return data, len(pii), pii


# Creating object for cv

transformcvobject = Transformation(extracted_cv)

maskeddata_cv, countcv, maskeddatacv = transformcvobject.masking_on_data()

# creating object for job description
transformjobdesobject = Transformation(extracted_jobrequirements)

maskeddata_jobsdes, count_jobsdes, maskeddatajobsdex = transformjobdesobject.masking_on_data()

useremail = all_email[0]
