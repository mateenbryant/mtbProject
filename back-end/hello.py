

from decimal import Decimal
from flask import Flask, jsonify, request
from flask import render_template
from bs4 import BeautifulSoup
from enum import Enum
from flask_cors import CORS, cross_origin
import requests


app = Flask(__name__)
CORS(app, support_credentials=True)



@app.route("/")
@cross_origin(supports_credentials=True)
def hello_world():
    r = requests.get("https://www.localconditions.com/weather-massanutten-virginia/va281/past.php")
    soup = BeautifulSoup(r.text, 'html.parser')
    x = soup.find("div", {"id": "accordion-paneled"})
    children = x.findChildren("div", recursive=False)
    rain_list = list()
    listSize = 0

    for child in children:
        rainfall_amount = child.find_all("span")[-1].next_sibling
        if (rainfall_amount == ":  in.") :
            rainfall_amount = 0.0
            if (listSize < 25) :
                rain_list.append(rainfall_amount)
                listSize += 1
        else :
            value = Decimal(rainfall_amount[2:6])
            floatVal = float(value)
            if (listSize < 25) :
                rain_list.append(floatVal)
                listSize += 1
        print(rainfall_amount)

    trail_conditions_enum = determine_trail_condition(rain_list)

    data = { 
        'last_25_days_precipitation' : rain_list,
        'trail_condition_description' : trail_conditions_enum.value
    }

    

    return jsonify(data)

def determine_trail_condition(recent_precipitation_list):
    sumVal = sum(recent_precipitation_list)
    # rule of thumb, for every inch of rain, wait one day for trail to dry off
    if (sumVal >= 0.0 and sumVal < 0.25) :
        return Trail_conditions.OK_CONDITIONS
    elif (sumVal >= .25 and sumVal < .5) :
        return Trail_conditions.GREAT_CONDITIONS
    elif (sumVal >= .50 and sumVal < .75) :
        return Trail_conditions.MEDIOCRE_CONDITIONS
    elif (sumVal >= .75 and sumVal < 1.0) :
        return Trail_conditions.BAD_CONDITIONS
    else :
        return Trail_conditions.UNRIDEABLE_CONDITIONS

    
    # Determine 72 hr rainfall amount

    # Switch case for which enum to return
    return
     
class Trail_conditions (Enum):
    OK_CONDITIONS = "Zero rain, trails are dry."
    GREAT_CONDITIONS = "More than a quarter-inch, prime conditions"
    MEDIOCRE_CONDITIONS = "More than half an inch of rain, okay"
    BAD_CONDITIONS = "More three-quarters of an inch, get muddy"
    UNRIDEABLE_CONDITIONS = "More than one inch, trails are not rideable."
    