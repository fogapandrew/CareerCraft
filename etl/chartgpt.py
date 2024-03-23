from transform import useremail
import utilities
import openai
from dotenv import load_dotenv
import os
from transform import maskeddata_cv, maskeddata_jobsdes

load_dotenv()  # take environment variables from .env


masked_cv, masked_job = utilities.fetch_maskedcv_jobdes(useremail)


API_KEY = os.getenv("API_KEY")

openai.api_key = API_KEY

# prompt engineering the openai with maskedcv and job description with questions.

input = f'''
Below you will find two masked data; masked cv and masked job description and requirements :

Here is the masked cv :

{maskeddata_cv}

Here is the job description and requirements :

{maskeddata_jobsdes}

Can you do the following :
if there is a 70% match in skills of cv and job descriptions and requiremetns or match in education do this:
    - provide details advices on areas to update on cv to suits the job description.
    - provide detailed motivation letter for the job as specify in the masked job description above.
    - provide detailed cover letter for this job also.
    No yapping!
if there is less than 50% in skills of cv and job descriptions and requiremetns do this:
    - provide a detail carreer path that the use can take to do this particular jobs, provide resources and links for courses that can be taken.
    No yapping!
'''

input_messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Bellow you will find a list of prompts questions..."},
    {"role": "user", "content": f"{input}"}
    # Add more user or assistant messages as needed
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=input_messages,
    temperature=0.7
)

# Parse the JSON string
response_dict = response

# Access and print the content field
responses = response_dict['choices'][0]['message']['content']

print(responses)

filesname = "example_document.docx"

utilities.save_text_as_word(responses, filesname)
