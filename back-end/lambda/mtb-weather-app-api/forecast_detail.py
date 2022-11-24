from dataclasses import dataclass
from config import app_config
from bs4 import BeautifulSoup
from decimal import Decimal
from enum import Enum
import requests

@dataclass
class LocationForecastDetail:
    last_25_days_precipitation: list[str]
    trail_conditions_descriptions: str
    forecast_descriptions: list[object]

def get_forecast_detail_for_location(location):
    historical_precipitation_list = get_historical_precipitation_list(location)

    return LocationForecastDetail(
        last_25_days_precipitation=historical_precipitation_list,
        forecast_descriptions=get_forecast_descriptions_list(location),
        trail_conditions_descriptions=get_computed_trail_conditions_forecast(historical_precipitation_list)
    )

def send_http_request(url):
    try:
        # 10 second timeout
        response = requests.get(url, timeout=10)
        # Raises an exception for HTTP status codes >= 400
        response.raise_for_status()
    except Exception as e:
        print("An error occurred while sending HTTP request to " + url)
        print(e)

    return response

def get_forecast_descriptions_list(location_name):
    url = app_config.get_forecast_api_url_for_location(location=location_name)
    response = send_http_request(url)
    if response.ok is False: return []

    daily_forecast_list = response.json()
    return daily_forecast_list["properties"]["periods"][0:4]


def get_historical_precipitation_list(location_name):
    url = app_config.get_precipitation_data_url_for_location(location=location_name)
    response = send_http_request(url)
    if response.ok is False: return []

    soup = BeautifulSoup(response.text, 'html.parser')
    x = soup.find("div", {"id": "accordion-paneled"})
    children = x.findChildren("div", recursive=False)
    rain_list = list()

    for child in children:
        if len(rain_list) >= 25: break
        rainfall_amount_text = child.find_all("span")[-1].next_sibling
        rainfall_amount = 0.0 if rainfall_amount_text == ":  in."  else float(Decimal(rainfall_amount_text[2:6]))
        rain_list.append(rainfall_amount) 

    return rain_list

def get_computed_trail_conditions_forecast(historical_precipitation_list):
    if not historical_precipitation_list: return "Could not estimate trail conditions due to insufficient/missing data."
    return determine_trail_condition(historical_precipitation_list[:4]).value

def determine_trail_condition(recent_precipitation_list):
    sumVal = sum(recent_precipitation_list)
    # rule of thumb, for every inch of rain, wait one day for trail to dry off
    if (sumVal >= 0.0 and sumVal < 0.25) :
        return TrailConditions.OK_CONDITIONS
    elif (sumVal >= .25 and sumVal < .5) :
        return TrailConditions.GREAT_CONDITIONS
    elif (sumVal >= .50 and sumVal < .75) :
        return TrailConditions.MEDIOCRE_CONDITIONS
    elif (sumVal >= .75 and sumVal < 1.0) :
        return TrailConditions.BAD_CONDITIONS
    else :
        return TrailConditions.UNRIDEABLE_CONDITIONS

     
class TrailConditions (Enum):
    OK_CONDITIONS = "Zero rain, trails are dry."
    GREAT_CONDITIONS = "More than a quarter-inch, prime conditions"
    MEDIOCRE_CONDITIONS = "More than half an inch of rain, okay"
    BAD_CONDITIONS = "More three-quarters of an inch, get muddy"
    UNRIDEABLE_CONDITIONS = "More than one inch, trails are not rideable."
  