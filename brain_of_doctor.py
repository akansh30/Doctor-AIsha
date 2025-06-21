#Step 1 : Setup GROQ API Key
import os
from dotenv import load_dotenv

load_dotenv() #loading env variables from .env file

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

#Step 2 : Convert Image to required format
import base64
#image_path="acne.jpg"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


#Step 3:  Setup Multimodal LLM
from groq import Groq

query="Is there anything wrong with my face?"
model="meta-llama/llama-4-scout-17b-16e-instruct"

def analyze_image_with_query(query, model, encoded_image):
    client = Groq(api_key=GROQ_API_KEY)
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}"
                    }
                }
            ]
        }
    ]
    chat_completion = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return chat_completion.choices[0].message.content