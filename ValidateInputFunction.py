import json

def lambda_handler(event, context):
    
    required_fields = ["id", "name", "age"]
    
    missing = [field for field in required_fields if field not in event]
    
    if missing:
        return {
            "status": "FAILED",
            "missing_fields": missing
        }
    
    return {
        "status": "SUCCESS",
        "message": "Validation Passed"
    }
