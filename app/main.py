import uuid
from random import randint

import aioboto3
from fastapi import FastAPI

app = FastAPI()


@app.get("/dynamodb")
async def dynamo_get():
    async with aioboto3.resource('dynamodb', region_name='eu-central-1') as dynamo_resource:
        table = await dynamo_resource.Table('random_uuid')
        result = await table.get_item(Key={'uuid': str(uuid.uuid4())})
        return result.get('Item')


@app.post("/dynamodb")
async def dynamo_post():
    async with aioboto3.resource('dynamodb', region_name='eu-central-1') as dynamo_resource:
        table = await dynamo_resource.Table('random_uuid')
        await table.put_item(Item={'uuid': str(uuid.uuid4())})
        return


@app.get("/healthcheck")
def healthcheck():
    return "OK"


@app.get("/")
async def root():
    return randint(0, 100000)
