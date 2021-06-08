"""
Note that for this flask app, we have a "templates" folder. 

This is where we'll store existing HTML files that we'd like to render according to our python logic."
"""

#Same setup as before - remember to run export FLASK_APP=app.py!

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/different_template")
def diff():
    return render_template('different_template.html')