import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

symbols = ["NIFTY50", "GOLD", "SENSEX"]

while True:
    event = {
        "event_type": "PRICE_UPDATED",
        "instrument": random.choice(symbols),
        "price": round(random.uniform(100, 500), 2),
        "timestamp": time.time(),
    }

    producer.send("market.price.updates", value=event)
    print("Produced:", event)

    time.sleep(3)
