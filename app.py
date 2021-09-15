from flask import Flask, render_template, request
from flask.templating import render_template
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)
from stories import story
# the toolbar is only enabled in debug mode:

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'secret'
toolbar = DebugToolbarExtension(app)
app.debug = True

inputs1 = story.prompts
@app.route('/')
def home_page():
    """Return Homepage"""
    return render_template("madlibs.html", inputs1=inputs1)

@app.route('/response')
def test():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]

    return render_template("response.html", place = place, noun = noun, verb = verb, adjective = adjective, plural_noun = plural_noun )
