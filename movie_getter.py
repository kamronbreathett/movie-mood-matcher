from dotenv import load_dotenv
from flask import Flask
import requests
import ollama

load_dotenv()


app = Flask(_name_)

@app.route("/")
def main_body():
    return render_template('index.html')


def call_AI(prompt):
    response = ollama.chat(model='gemma3', messages=[
        {
            'role': 'user',
            'content': prompt
        },
    ])

    return response['messages']['content']

    #We have responses but we need to call the API to retrieve movies from TMDb



def movie_responses(prompt):
    #Change body html & get AI response & AI has to call API function
    call_AI(prompt)

    #We have responses but 