import uuid

import aioboto3
import boto3
from fastapi import FastAPI

app = FastAPI()
# dynamodb_synch = boto3.resource('dynamodb', region_name='eu-central-1')
# dynamodb_asynch = await aioboto3.resource('dynamodb', region_name='eu-central-1')
#
#
# @app.get("/dynamodb-synch")
# def dynamo_get_synch(param=None):
#     table = dynamodb_synch.Table('random_uuid')
#     result = table.get_item(Key={'uuid': param or str(uuid.uuid4())})
#     return result.get('Item', 'Not found')
#
#
# @app.post("/dynamodb-synch")
# def dynamo_post():
#     table = dynamodb_synch.Table('random_uuid')
#     result = table.put_item(Item={'uuid': str(uuid.uuid4())})
#     return result['Item']
#
#
# @app.get("/dynamodb-asynch")
# async def dynamo_get(param=None):
#     table = await dynamodb_asynch.Table('random_uuid')
#     result = await table.get_item(Key={'uuid': param or str(uuid.uuid4())})
#     return result.get('Item', 'Not found')
#
#
# @app.post("/dynamodb-asynch")
# async def dynamo_post():
#     table = await dynamodb_asynch.Table('random_uuid')
#     result = await table.put_item(Item={'uuid': str(uuid.uuid4())})
#     return result['Item']


@app.get("/healthcheck")
def healthcheck():
    return "OK"


@app.get("/")
async def root():
    return "OK"
