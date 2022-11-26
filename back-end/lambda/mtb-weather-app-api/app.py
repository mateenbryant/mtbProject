
import jsonpickle
from config import get_locations_with_image_urls
from forecast_detail import get_forecast_detail_for_location

def lambda_handler(event, context):

    url_path = event['path']
    if 'forecast-detail' in url_path:
        location = event['pathParameters']['location']
        lambda_response = get_forecast_detail_for_location(location)
    elif url_path == '/locations':
        lambda_response = get_locations_with_image_urls()
    else:
        raise RuntimeError

    return {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": jsonpickle.encode(lambda_response, unpicklable=False)
    }
