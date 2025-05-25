
Day 1:
Created Templates and base HTML/CSS files
Figuring out the design of the website

Day 2:
Officially setting up Flask application with routes
Downloaded the Ollama model that we need to use

Day 3:
 Day 2 continued
 Created and styled search button while creating the space for the results to be entered.

Day 4:
Still creating information from Day 2 & 3 now I am creating the format.

Day 5:
Setting up and testing Ollama model for use
Finished having Ollama setup now connection to the HTML is needed

Day 6:
Creating TMDb tool for the model to use
Creating JavaScript Effects for increased user effects.

Day 7:
Still creating Ollama tool to find movies based off of prompt using the TMDb API
Created Ollama system prompt and getMovie API GET function; troubleshooting no results being returned

Day 8:
Finished Ollama tool
Creating CSS for a base, more professional look
Finished CSS

Day 9:
Found Ollama not running with assistant role
Need to fix Ollama assistant not running now we need to change results when the user enters a new mood
bar not updating when user puts a new search input 
Final Fix


Problems Encountered & Fixes:

First Problem:
Ollama Model Selection

First Solution:
Some Ollama models don't support prompt roles such as system or assistant. There are also some model that also don't support tool usage. The Ollama 3.1:8b model supports both so that's why its being used.

Second Problem:
System Prompt Usage

Second Solution:
The System Prompt MUST declare the models usage as a movie recommender that CREATES a query based on the movie that is a MOVIE, and it must reinforce that it has to use the tool.