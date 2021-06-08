"""TO RUN THIS FILE:

Get in the folder in which this flask_basic.py file lives. 

Set which file is the main flask app in this folder via in your terminal with: 
    export FLASK_APP=api.py
    
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

#Note the <> around our template here: this will allow us to only return data about any category we want.
@app.route("/data/major-category/<majcat>.csv")
def maj_cat(majcat):
    import pandas as pd
    df = pd.read_csv('https://raw.githubusercontent.com/benartuso/nodef19/master/data/03-vis-aesthetics/recent-grads.csv')
    filtered = df[df.Major_category==majcat]
    return filtered.to_csv()

@app.route("/analysis/major-category/<majcat>.csv")
def major_cat_stats(majcat):
    import pandas as pd
    df = pd.read_csv('https://raw.githubusercontent.com/benartuso/nodef19/master/data/03-vis-aesthetics/recent-grads.csv')
    filtered = df[df.Major_category==majcat]
    share_women = filtered.ShareWomen.mean()
    average_salary = filtered.Median.mean()
    return "Average fraction of women among " + majcat + " majors: " + str(share_women) + """<br>
    Average median salary among these majors: """ + str(average_salary) 


