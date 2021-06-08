"""TO RUN THIS FILE:

Get in the folder in which this flask_basic.py file lives. 

Set which file is the main flask app in this folder via in your terminal with: 
    export FLASK_APP=flask_basic.py
    
In the folder, say "flask run"

DO NOT call this or any other files "flask.py"
   
 
 """

#From the flask package, import the Flask class to make our app.
from flask import Flask

#Create our flask application.
app = Flask(__name__)

#Establish a route for when people visit the main page of our application. 
#Then, define a function that will run when that happens.
@app.route("/")
def hello_world():
    return "Welcome to the main page!"

#Different route, and function, for the "projects" page: 
@app.route("/projects")
def projects():
    return "We have 3 projects in Launch"


#And another, for the tracks page. Note, we can insert some basic html tags. 
@app.route("/tracks")
def tracks():
    return """<h1>We have 4 tracks, data is the best.</h1>
               <a href="/">Go back to the main page</a>
               <a href="projects">Go to the project page</a>
               """
            
             

