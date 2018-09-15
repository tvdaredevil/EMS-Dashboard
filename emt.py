#!flask/bin/python
from flask import Flask, request, render_template,redirect
import json

app = Flask(__name__)

try:
    with open('data.json') as f:
        NAME_ARR = json.load(f)
except:
    NAME_ARR = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submitData', methods=['POST'])
def submitData():
    obj = {
        "name": request.form["name"],
        "condition": request.form["condition"],
        "occupancy": request.form["occupancy"],
        "location": request.form["location"],
        "capacity": request.form["capacity"]
        #"grade": ____
    }
    added = 0;i=0
    for p in NAME_ARR:
        if p['name'] == request.form["name"]:
            NAME_ARR[i] = obj
            added = 1
            break
        i=i+1
    if not added:
        NAME_ARR.append(obj)
    with open('data.json', 'w') as outfile:
        json.dump(NAME_ARR, outfile)
    return redirect('/addData')

@app.route('/addData')
def addData():
    return render_template('addData.html')

@app.route('/api/listPeople')
def listPeople():
    return json.dumps(NAME_ARR)


if __name__ == "__main__":
    app.run(debug=True)
