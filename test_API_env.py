import os

from dotenv import load_dotenv, find_dotenv

load_dotenv() 

openai_api_key = os.environ['OPENAI_API_KEY']

print(openai_api_key)