from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "shhhhh"

@app.route("/")
def show_form():
    """Shows form inputs"""

    prompts = story.prompts
    return render_template("form.html", prompts=prompts)

@app.route("/story")
def show_story():
    """Shows results"""
    text = story.generate(request.args)
    return render_template("story.html", text=text)
