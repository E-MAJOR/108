# instead of npm (node project manager) in js, use pip for py python -m pip --version, need put on top of python a framework (flask or **django)
# using flask to use with API, but need force into the folder instead the operating system, requiring shield around folder (virtual environment) python -m pip install venv
# mac:sudo python3 -m pip install virtualenv
# win:python -m pip install virtualenv
# python server.py to run

from flask import Flask #class with upper case F
from mock_data import catalog
import json

#magic functions/variables __name__
app = Flask(__name__) #to create new application in Flask, with name of "Main", don't need word new Flask()

me = {
        "name": "Mark",
        "last": "Courtright",
        "age": 56,
        "hobbies": [],
        "address": {
            "street": "Jimray",
            "number": 123,
            "city": "Mishawaka"
        }
    }

@app.route("/") #a decorator, defining end points in route
#127.001 local host, not on net
#this part is python, everything else is flask
def home():  
    return "Hello from Python"

@app.route("/test") #also a get request, by default
def test_function():
    return "I'm a test function"

#return full name getting value from dictionary
@app.route("/about")  #url is /about, catch url code and return something
def about():
    return me["name"] + " " + me["last"] #dictionary exists global

#--------------------------------------------------------
#------------------API ENDPOINTS------------------------
#--------------------------------------------------------

@app.route("/api/catalog")
def get_catalog():
    return json.dumps(catalog)  #later to be done from database, now mock_data, need to put into .JSON, not plain data, wont work without import json 

@app.route("/api/cheapest")
#catalog is a global list of dictionaries
def get_cheapest():
    cheapest = catalog[0]
    for product in catalog:
        print(product["price"])
        if cheapest["price"] > product["price"]:
            cheapest = product
    return json.dumps(cheapest)

@app.route("/api/product/<id>") #<id> is a variable, that you fill in with the _id number from the catalog, it will find the product and return it
def get_product(id):
    for product in catalog:
        if product["_id"] == id:
            return json.dumps(product)

    return "DNE"



app.run(debug=True) # to run app


#Rest API = "API", intermediary allows connect 2 systems, present easy to read interface, establish rules, Application Programming Interface, across the web = web api's = web services, with robo-waiters serving data to apps or websites with menu of data available, to add "+" source code, served as .JSON {} or .XML <>file
# {"video":{"id": "xxx","published":"xxx", "title":"xxx"}}
# <video> <id>xxx <published>xxx <title>xxx </video>
#google company huge with free/open API's call URL in their site, get served data back, but cannot access to change their code, with restrictions, before serving data, secret google indo protected, "the gate keeper"
#rest api's to post, delete, get 90% use .JSON strings, but.XML is more secure, by default api's = GET