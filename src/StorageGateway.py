import os

import boto3


class StorageGateway:
    def __init__(self):
        if os.environ.get('IS_OFFLINE'):
            self.__storage = boto3.resource(
                'dynamodb',
                region_name='localhost',
                aws_access_key_id='your_key_id',
                aws_secret_access_key='your_secret_key',
                endpoint_url='http://localhost:8000',
            )
        else:
            self.__storage = boto3.resource('dynamodb')

    def get(self):
        return self.__storage
