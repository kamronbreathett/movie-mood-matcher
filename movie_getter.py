from dotenv import load_dotenv
import requests
from llama_index.llms.ollama import Ollama
import ollama
import os
import json
import random

load_dotenv()

def call_AI(prompt):
    print("Function call_AI started")
    response = ollama.chat(model='llama3.1:8b', messages=[
        {
            'role': 'system',
            'content': "You are a movie recommendation expert. When a user provides a mood or theme, respond with a function call to 'get_Movie' using a relevant movie name. Do NOT provide direct answers—ALWAYS use the tool.",
        },
        {
            'role': 'user',
            'content': prompt,
        }
        ],
        tools=[get_Movie]
    )

    available_functions = {
        'get_Movie': get_Movie,
    }

    for tool in response.message.tool_calls or []:
        function_to_call = available_functions.get(tool.function.name)
        if function_to_call:
            print('Function output:', function_to_call(**tool.function.arguments))
            return function_to_call(**tool.function.arguments)
        else:
            print('Function not found:', tool.function.name)
            return 'Movie does not exist'

    print("Tool Calls:", response.message.tool_calls)


    #We have responses but we need to call the API to retrieve movies from TMDb

def get_Movie(query):
    words = query
    url = f"https://api.themoviedb.org/3/search/movie?query={words}&include_adult=false&language=en-US&page=1"
    token = os.getenv('AUTHRIZATION_KEY')
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    respons = requests.get(url, headers=headers)
    rte = respons.json()
    x = random.randint(0, len(rte.get("results")) -1 )
    titles = rte.keys()
    title = rte.get("results")[x]['original_title']
    image = rte.get("results")[x]['poster_path']
    return title