import jsonpickle
from config import get_locations_with_image_urls
from forecast_detail import get_forecast_detail_for_location

def lambda_handler(event, context):

    response_headers = {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        }

    url_path = event['path']
    if 'forecast-detail' in url_path:
        location = event['pathParameters']['location']
        lambda_response = get_forecast_detail_for_location(location)

        # If error in response
        if len(lambda_response.forecast_descriptions) is 1:
            response_headers['Cache-Control'] = 'no-store, must-revalidate'
        else:
            response_headers['Cache-Control'] = 'max-age=3600'

    elif url_path == '/locations':
        lambda_response = get_locations_with_image_urls()
        response_headers['Cache-Control'] = 'max-age=3600'
    else:
        raise RuntimeError

    return {
        "statusCode": 200,
        "headers": response_headers,
        "body": jsonpickle.encode(lambda_response, unpicklable=False)
    }