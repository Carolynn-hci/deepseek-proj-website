from openai import OpenAI

#following imports to allow API key to be loaded
import os
from dotenv import load_dotenv
from pathlib import Path

import json #for testing 


dotenv_path = Path('../wesbite_ds/.env')
load_dotenv(dotenv_path= dotenv_path)

def Event_source_stream(
    messages = [{"role": "system", "content": "You are a helpful assistant. \
             Keep responses to a maximum of 100 words.\
                If code is asked, try to keep it as efficient as possible. Include only one method for one use,\
                 making any assumptions if neccessary.\
                 There is no need to include the word count at the end of your response."
             }
             ], prompt = ''
             ):
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

    
    