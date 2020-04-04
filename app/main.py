import uuid

import aioboto3
from fastapi import FastAPI

app = FastAPI()


@app.get("/dynamodb")
async def dynamo_get(param=None):
    async with aioboto3.resource("dynamodb", region_name='eu-central-1') as dynamo_resource:
        table = dynamo_resource.Table('random_uuid')
        result = await table.get_item(Key={'uuid': param or str(uuid.uuid4())})
        return result.get('Item', 'Not found')


@app.post("/dynamodb")
async def dynamo_post():
    async with aioboto3.resource("dynamodb", region_name='eu-central-1') as dynamo_resource:
        table = dynamo_resource.Table('random_uuid')
        result = await table.put_item(Item={'uuid': str(uuid.uuid4())})
        return result['Item']


@app.get("/healthcheck")
async def asdf():
    return "OK"
