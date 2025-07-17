from openai import OpenAI

#following imports to allow API key to be loaded
import os
from dotenv import load_dotenv
from pathlib import Path

import json #for testing 


module_dir = os.path.dirname(__file__)
dotenv_path = Path('../wesbite_ds/.env')
load_dotenv(dotenv_path= dotenv_path)

def get_prompts():
    file_path = os.path.join(module_dir, 'learning_mode_prompts.txt')
    with open(file_path,'r') as file:
        data = file.readlines()
        data = ''.join(data)
    return data

def Event_source_stream(prompt = ''):
    content = get_prompts()
    messages = [{"role": "system", "content": content
             }
             ]
    messages.append({'role':'user', 'content':prompt})

    ###test
    KEY = os.getenv('DS_API_KEY')
    client = OpenAI(api_key= KEY, 
                    base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages = messages,
        stream=True
    )
    reply = ''
    for line in response:
            
            chunk = json.dumps( {'content':line.choices[0].delta.content } )
            reply += chunk
            yield 'data: %s\n\n' %chunk
            
            if line.choices[0].finish_reason:
                 yield 'data: finc\n\n'
    latest = {"role": "assistant", "content": reply }
    #print(reply)
    messages.append(latest)

    
    