from transform import useremail
import utilities
import openai


masked_cv, masked_job = utilities.fetch_maskedcv_jobdes(useremail)

openai.api_key = "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"

# prompt engineering the openai with maskedcv and job description with questions.

input = f'''
Below you will find two masked data; masked cv and masked job description and requirements :

Here is the masked cv :

{masked_cv}

Here is the job description and requirements :

{masked_job}

Can you do the following :
- update the cv to suit the job description and requirements.
- provide detailed motivation letter for this job.
- provide detailed cover letter for this job.

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
