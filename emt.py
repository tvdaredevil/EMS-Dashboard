#!flask/bin/python
from flask import Flask, request
import json

app = Flask(__name__)


with open('data.json') as f:
    NAME_ARR = json.load(f)

@app.route('/')
def index():
    return """
        <form action="/submitData" method="POST">
            <p>Yo</p>
            <input name='name' placeholder='Zone a, zone b ... zone n'>
            <input name='condition' placeholder='Enter your condition'>
            <input name='occupancy' placeholder='Enter your occupancy'>
            <input name='location' placeholder='Enter your location'>
            <input name='capacity' placeholder='Enter your capacity'>
            <button type='submit'>Submit Data!!</button>
        </form>
        <form action="/editZone" method="POST">
            <button type='edit'>Edit!!</button>
        </form>
    """

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
    return """<p>Saved data!</p>
    <form action="/">
        <button type='Go Back'>Go Back</button>
    </form>"""

@app.route('/editZone', methods=['POST'])
def edit():

    return """
        <form action="/edited" method="POST">
            <p>yo</p>
            <input name='name' placeholder='Zone a, zone b ... zone n'>
            <input name='condition' placeholder='Enter the condition'>
            <input name='occupancy' placeholder='Enter occupancy'>
            <input name='location' placeholder='Enter location'>
            <input name='capacity' placeholder='Enter capacity'>
            <button type='submit'>Submit new Data!</button>
        </form>
    """


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
    return """<form action="/">
        <button type='Go Back'>Go Back</button>
    </form>"""

@app.route('/api/listPeople')
def listPeople():
    return json.dumps(NAME_ARR)


if __name__ == "__main__":
    app.run(debug=True)
