import json
import time
from kafka import KafkaConsumer
import boto3
from datetime import datetime

BUCKET_NAME = "your-s3-bucket-name"

consumer = KafkaConsumer(
    "crypto-prices",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

s3 = boto3.client("s3")

for message in consumer:

    event = message.value
    now = datetime.utcnow()

    key = f"crypto-data/year={now.year}/month={now.month}/day={now.day}/event_{int(time.time())}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=json.dumps(event)
    )

    print("Uploaded:", key)
