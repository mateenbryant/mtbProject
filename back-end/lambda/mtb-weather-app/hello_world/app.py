import json
from bs4 import BeautifulSoup
from enum import Enum
import requests
from decimal import Decimal

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    try:
        print("This is a test")
        data = get_park_trail_condition_and_forecast_details()
        print(json.dumps(data))
        print(data)
    except Exception as e:
        print("Another test")
        print(e)

    return {
        "statusCode": 200,
        "body": json.dumps(get_park_trail_condition_and_forecast_details())
    }


location_name_to_latlong_map = {
    'massanutten' : 'LWX/40,42',
    'bryce' : 'sdfsd'
}

def get_forecast_descriptions(location_name):
    grid_value = location_name_to_latlong_map[location_name]

    url = "https://api.weather.gov/gridpoints/" + grid_value + "/forecast"
    print("Last test")
    response_json = requests.get(url).json()
    print(response_json)
    daily_forecast_list = response_json
    return daily_forecast_list["properties"]["periods"][0:4]
    

def get_park_trail_condition_and_forecast_details():
    print("Test before first request")
    r = requests.get("https://www.localconditions.com/weather-massanutten-virginia/va281/past.php")
    soup = BeautifulSoup(r.text, 'html.parser')
    x = soup.find("div", {"id": "accordion-paneled"})
    children = x.findChildren("div", recursive=False)
    rain_list = list()
    listSize = 0

    print("Test 2")

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

    print("Test 3")
    forecast_descriptions_list = get_forecast_descriptions("massanutten")
    print(forecast_descriptions_list)
    data = { 
        'last_25_days_precipitation' : rain_list,
        'trail_condition_description' : trail_conditions_enum.value,
        'forecast_descriptions' : forecast_descriptions_list
    }
    return data

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
    