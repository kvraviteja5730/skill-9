import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Students")

def lambda_handler(event, context):
    
    # Original input is preserved at root
    item = {
        "id": event["id"],
        "name": event["name"],
        "age": event["age"]
    }
    
    table.put_item(Item=item)
    
    return {
        "status": "INSERTED",
        "item_id": event["id"]
    }
