This script is created to perform mass departure gate change in Sabre Movement Control via MCEG rest api
Date and Time values must be in UTC and 24 hr format
Date must be follow YYYYMMDD string format
example Date: 20200130
example Time: 2346

Before running the script:
1- make sure flight data is populated correctly in data.csv (do not change column name, script will throw error)
2- in config.json file make sure correct "MVT" environment, "post_dep_gate_url" and "how_many_gate_change_per_flight" is set

Note: "how_many_gate_change_per_flight" is the upper limit. 
    If its 10 then script will run for 10 minute with 10 gate change request per flight.
    If its 50 then it will run for 50 minute same way. Adjust the values accordingly.

To run the script:
1- Make sure python 3.8 or later version installed in your system
2- from command line, navigate to folder where you saved these files and type: python script.py  and press Enter key
