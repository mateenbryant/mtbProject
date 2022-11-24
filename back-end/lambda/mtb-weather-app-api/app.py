
import jsonpickle
from config import get_locations_list
from forecast_detail import get_forecast_detail_for_location

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

    url_path = event['path']
    if 'forecast-detail' in url_path:
        location = event['pathParameters']['location']
        lambda_response = get_forecast_detail_for_location(location)
    elif url_path == '/locations':
        lambda_response = get_locations_list()
    else:
        raise RuntimeError

    return {
        "statusCode": 200,
        "body": jsonpickle.encode(lambda_response, unpicklable=False)
    }
