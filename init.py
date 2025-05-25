from flask import Flask, render_template, request
from movie_getter import call_AI, get_Movie

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/movie")
def movie_getter():
    prompts = request.args.get('bar')
    reset = call_AI(prompts)
    return render_template('movie.html', results = reset)

if __name__ == "__main__":
    app.run()
