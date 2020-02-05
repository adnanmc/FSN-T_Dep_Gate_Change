from pathlib import Path
import urllib.request
import json
import datetime
import time
import string
import random
import csv

# read config file
configFilePath = Path("./config.json")
with open(configFilePath) as json_file:
    data = json.load(json_file)
    url = data.get("post_dep_gate_url")
    stg = data.get("MVT")
    limit = data.get("how_many_gate_change_per_flight")
    limit = int(limit)

# read test data   
csvPath = Path("./data.csv")
data = csv.DictReader(open(csvPath, 'r'))
testData = list()
for flight in data:
    testData.append(flight)


# generate random gate 4 char
def gate_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Function for making post request
def post_gate_change(url, params):
    params = json.dumps(params).encode("utf8")
    req = urllib.request.Request(url=url, data=params, method = "POST")

    # Add the appropriate header.
    req.add_header("Content-type", "application/json; charset=UTF-8")
    response = urllib.request.urlopen(req)
    response = json.loads(response.read().decode('utf8'))
    return response
    
# perform gate change 
for x in range(0, limit):
    depGate = gate_generator()
    print(depGate)
    for flight in testData:
        flightNum = flight.get("flightNum")
        utcOriginDate = flight.get("utc_dep_date")
        origin = flight.get("origin")
        destination = flight.get("destination")
        stdUTC = flight.get("utc_dep_time")
        jsonBody = {"stg": f"{stg}",
                    "flightNum": f"{flightNum}",
                    "utcOriginDate": f"{utcOriginDate}",
                    "origin": f"{origin}",
                    "destination": f"{destination}",
                    "stdUTC": f"{stdUTC}",
                    "depGate": f"{depGate}"}
        # print(jsonBody)
        response = post_gate_change(url, jsonBody)
        responseError = response.get("error")
        if responseError != None:
            print(responseError)

    # wait 60 sec after the messages are sent
    time.sleep(60)
