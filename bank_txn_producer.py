import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

while True:
    event = {
        "event_type": "BANK_TXN_CREATED",
        "client_id": f"C{random.randint(1,5)}",
        "account_id": f"A{random.randint(1,10)}",
        "amount": random.randint(-5000, 5000),
        "timestamp": time.time(),
    }

    producer.send("bank.transactions", value=event)
    print("Produced:", event)

    time.sleep(2)
