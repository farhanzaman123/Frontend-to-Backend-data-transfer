import json
import boto3
import secrets
def lambda_handler(event, context):
    # TODO implement
    click_id=event["name"]
    dynamodb=boto3.client('dynamodb')
    click_key=secrets.token_urlsafe(16)
    dynamodb.put_item(TableName="click_farm",Item={"click_id":{"S":click_id}})
    return {
        'statusCode': 200,
        'headers': {"Content-Type" : "application/json",
            "Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Methods" : "OPTIONS,POST","GET"
            "Access-Control-Allow-Credentials" : True,
            "Access-Control-Allow-Origin" : "",
            "X-Requested-With" : ""},
        'body': json.dumps('Hello from Lambda!')
    }
