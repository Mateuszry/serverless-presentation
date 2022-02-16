import json
import logging
import os
import uuid

from src.StorageGateway import StorageGateway


def lambda_handler(event, context):
    try:
        logging.warning(f"Create note request body: {event.get('body')}")
        note = json.loads(event.get("body"))
        note['id'] = uuid.uuid4().hex

        storage = StorageGateway().get()
        table = storage.Table(os.environ['NOTE_TABLE'])
        table.put_item(Item=note)

        response: dict = {
            "statusCode": 201,
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
