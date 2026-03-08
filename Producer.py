import json
import time
import requests
from datetime import datetime
from kafka import KafkaProducer

API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    try:
        response = requests.get(API_URL)
        data = response.json()

        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "source": "coingecko",
            "data": data
        }

        producer.send("crypto-prices", event)
        producer.flush()

        print("Sent event:", event)

    except Exception as e:
        print("Producer error:", e)

    time.sleep(30)
