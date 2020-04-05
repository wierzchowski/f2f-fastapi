import os
import uuid
from random import randint

import aioboto3
import databases
import sqlalchemy
from fastapi import FastAPI

DATABASE_URL = os.environ.get('DATABASE_URL')
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

uuid_table = sqlalchemy.Table(
    "uuid",
    metadata,
    sqlalchemy.Column("uuid", sqlalchemy.String)
)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


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


@app.post('/rds')
async def rds_post():
    data = str(uuid.uuid4())
    query = uuid_table.insert().values(uuid=data)
    last_record_id = await database.execute(query)
    return {"id": last_record_id, 'uuid': data}


@app.get("/healthcheck")
def healthcheck():
    return "OK"


@app.get("/")
async def root():
    return randint(0, 100000)
