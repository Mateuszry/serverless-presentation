import json


def lambda_handler(event, context):
    body: dict = {
        'healthcheck': 'ok'
    }

    response: dict = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true",
        }
    }

    return response
