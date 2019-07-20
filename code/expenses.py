import json
from uuid import uuid4
import os

import boto3
from boto3.dynamodb.conditions import Key

def get(event,context):
    dynamodb = boto3.resource('dynamodb')
    expenses_table = dynamodb.Table(os.environ.get('ExpensesTable'))
    items = expenses_table.scan()['Items']
    body = {'expenses': items}
    return {'statusCode': 200, 'body': json.dumps(body)}
    
def post(event,context):
    print(event)
    #readcsv
    #Insert data on tale
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)   
    #for-loop logic
    table.put_item(
   Item={
        'username': 'janedoe',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
)

    return {"statusCode":"201"}