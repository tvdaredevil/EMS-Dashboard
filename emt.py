#!flask/bin/python
from flask import Flask, request, render_template,redirect
import json
from math import *

app = Flask(__name__)

try:
    with open('data.json') as f:
        ZONE_ARR = json.load(f)
except:
    ZONE_ARR = []

epicenter = {"lat": 33.4, "lng": -75.5}

def dist(lat1, lon1, lat2, lon2): 
    R = 6371e3
    toRad = pi / 180
    print lat1
    print lat2
    print lon1
    print lon2
    lat1, lat2, lon1, lon2 = [float(x) for x in [lat1, lat2, lon1, lon2]]
    phi_1 = lat1 * toRad
    phi_2 = lat2 * toRad
    delta_phi = (lat2-lat1) * toRad
    delta_lambda = (lon2-lon1) * toRad

    a = sin(delta_phi/2) * sin(delta_phi/2) + cos(phi_1) * cos(phi_2) * sin(delta_lambda/2) * sin(delta_lambda/2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    d = R * c
    return d

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
    obj['distance'] = dist(obj['lat'], obj['long'], epicenter['lat'], epicenter['lng'])
    added = 0;i = 0
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

@app.route('/api/getEpicenter')
def getEpicenter():
    return json.dumps(epicenter)


if __name__ == "__main__":
    app.run(debug=True)
