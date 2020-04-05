import uuid
from random import choice

import aioboto3
import boto3
from fastapi import FastAPI

app = FastAPI()
dynamodb_synch = boto3.resource('dynamodb', region_name='eu-central-1')
dynamodb_asynch = aioboto3.resource('dynamodb', region_name='eu-central-1')

conn_pool = [boto3.resource('dynamodb', region_name='eu-central-1') for _ in range(4)]


@app.get("/dynamodb-synch")
def dynamo_get_synch():
    table = dynamodb_synch.Table('random_uuid')
    result = table.get_item(Key={'uuid': str(uuid.uuid4())})
    return result.get('Item')


@app.post("/dynamodb-synch")
def dynamo_post():
    table = dynamodb_synch.Table('random_uuid')
    result = table.put_item(Item={'uuid': str(uuid.uuid4())})
    return result


@app.get("/dynamodb-asynch")
async def dynamo_get():
    table = dynamodb_asynch.Table('random_uuid')
    result = table.get_item(Key={'uuid': str(uuid.uuid4())})
    return result.get('Item')


@app.post("/dynamodb-asynch")
async def dynamo_post():
    resource = choice(conn_pool)
    table = resource.Table('random_uuid')
    result = table.put_item(Item={'uuid': str(uuid.uuid4())})
    return result


@app.get("/healthcheck")
def healthcheck():
    return "OK"


@app.get("/")
async def root():
    return "OK"
