import json
import logging
import os

from src.StorageGateway import StorageGateway


def lambda_handler(event, context):
    path_params: dict = event.get('pathParameters')

    try:
        storage = StorageGateway().get()
        table = storage.Table(os.environ['NOTE_TABLE'])
        item = table.get_item(Key={'id': path_params.get('id')})

        if "Item" not in item:
            raise Exception(f"Note with id '{path_params.get('id')}' does not exist")

        note = item.get('Item')

        response: dict = {
            "statusCode": 200,
            "body": json.dumps(note),
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": "true",
            }
        }
    except Exception as e:
        logging.warning(f"Request body: {event.get('body')}")
        logging.error(str(e), exc_info=True)
        response: dict = {
            "statusCode": e.code if hasattr(e, 'code') else 400,
            "body": str(e),
            "headers": {
                "Content-Type": "application/json",
            }
        }

    return response
