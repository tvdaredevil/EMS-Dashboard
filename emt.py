#!flask/bin/python
from flask import Flask, request, render_template,redirect
import json

app = Flask(__name__)

try:
    with open('data.json') as f:
        ZONE_ARR = json.load(f)
except:
    ZONE_ARR = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submitData', methods=['POST'])
def submitData():
    obj = {
        "name": request.form["name"],     # Label
        "status": request.form["status"], # Label
        "lat": request.form["lat"],               # Location
        "long": request.form["long"],             # Location
        "food": request.form["food"],             # Numerical
        "water": request.form["water"],           # Numerical
        "capacity": request.form["capacity"],     # Numerical
        "occupancy": request.form["occupancy"],   # Numerical
        "electricity": request.form["electricity"], # Boolean
    }
    #todo(karim): find distance and update OBJ
    added = 0;i=0
    for p in ZONE_ARR:
        if p['name'] == request.form["name"]:
            ZONE_ARR[i] = obj
            added = 1
            break
        i=i+1
    if not added:
        ZONE_ARR.append(obj)
    with open('data.json', 'w') as outfile:
        json.dump(ZONE_ARR, outfile)
    return redirect('/addData')

@app.route('/addData')
def addData():
    return render_template('addData.html')

@app.route('/api/listZones')
def listZones():
    return json.dumps(ZONE_ARR)


if __name__ == "__main__":
    app.run(debug=True)
