import json
import boto3
import random
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    bucket_name = 'bison-de-project'  
    
    data = []
    
    for _ in range(5):
        record = {
            "user_id": random.randint(100, 999),
            "event": random.choice(["view_product", "add_to_cart", "purchase"]),
            "product_id": random.randint(1000, 2000),
            "timestamp": datetime.utcnow().isoformat()
        }
        data.append(record)
    
    file_name = f"raw/data_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.json"
    
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(data)
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps("Data uploaded successfully")
    }






    
