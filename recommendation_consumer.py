from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "bank.transactions",
    "market.price.updates",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    group_id="recommendation-service",
    auto_offset_reset="earliest",
)

print("Recommendation service started...")

for message in consumer:
    event = message.value
    print("Consumed event:", event)

    # STUB logic
    if event["event_type"] == "BANK_TXN_CREATED":
        print("→ Evaluate client liquidity & suggest investment")
    elif event["event_type"] == "PRICE_UPDATED":
        print("→ Re-evaluate portfolio recommendations")
