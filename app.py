from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = 'chickensarecool'
toolbar = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    prompt = story.prompts
    return render_template("home.html", prompts=prompt)

@app.route('/story')
def run_story():
    text = story.generate(request.args)
    return render_template("story.html", text=text)