## LEVEL1: Simple form of communication
## Step L1.1: Load libraries and the key

##installing openai
###################################
#!pip install openai
##Setting an API key as
#!export OPENAI_API_KEY='sk-...'
## or aletnatively as import openai // openai.api_key = "sk-..."
import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

###################################
##Step L1.2:: define a responce function

def get_responce(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

##Step L1.3:: Ask a question
response = get_responce("How old is Barack Obama?")

## LEVEL2: Several instructions 
###################################
##Step L2.2:: define a responce function
def get_responce_complex(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness 
        max_tokens=max_tokens, # the maximum number of tokens the model can ouptut 
    )
    content = response.choices[0].message["content"]

    token_dict = {
'prompt_tokens':response['usage']['prompt_tokens'],
'completion_tokens':response['usage']['completion_tokens'],
'total_tokens':response['usage']['total_tokens'],
    }

    return content, token_dict
	
messages = [
{'role':'system', 
 'content':"""You are an startup advisor who responds\
 in the style of Paul Graham."""},    
{'role':'user',
 'content':"""give me some business advice \ 
 about startup advertising"""},  
] 
response, token_dict = get_responce_complex(messages)

print(response)
print(token_dict)
