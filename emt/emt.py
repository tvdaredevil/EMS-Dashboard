#!flask/bin/python
from flask import Flask, request, render_template
import json

app = Flask(__name__)


with open('data.json') as f:
    NAME_ARR = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submitData', methods=['POST'])
def submitData():
    NAME_ARR.append({
        "name": request.form["name"],
        "condition": request.form["condition"],
        "occupancy": request.form["occupancy"],
        "location": request.form["location"],
        "capacity": request.form["capacity"]
        #"grade": ____
    })
    with open('data.json', 'w') as outfile:
        json.dump(NAME_ARR, outfile)
    return render_template('submitData.html')

@app.route('/editZone', methods=['POST'])
def edit():
    return render_template('editZone.html')


@app.route('/edited', methods=['POST'])
def edited():
    for p in NAME_ARR:
        if p['name'] == request.form["name"]:
            p['condition'] == request.form["condition"]
            p['occupancy'] = request.form["occupancy"]
            p['location'] = request.form["location"]
            p['capacity'] = request.form["capacity"]
    print(NAME_ARR)
    with open('data.json', 'w') as outfile:
        json.dump(NAME_ARR, outfile)
    return render_template('edited.html')

@app.route('/api/listPeople')
def listPeople():
    return json.dumps(NAME_ARR)


if __name__ == "__main__":
    app.run(debug=True)
