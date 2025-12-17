# Kafka Event Bus – Test Skeleton

This repository contains a **minimal Kafka-based event bus skeleton** built to demonstrate how an **event-driven architecture** can work for Capera’s core use cases.

The goal of this skeleton is to:

* Prove Kafka as an **enterprise-wide event bus**
* Demonstrate **event production, consumption, and replay**
* Model real Capera events (bank transactions & market data)
* Keep everything **simple and demo-friendly**

---

## 1. Architecture Overview

```
Bank Transaction Producer  ─┐
                            ├──> Kafka (Event Bus) ──> Recommendation Consumer
Market Price Producer      ─┘                          (Workflow Stub)
```

* **Producers** simulate upstream systems (bank APIs, market feeds)
* **Kafka** acts as the central, durable event log
* **Consumers** represent downstream workflows (recommendations, analytics, alerts)

Kafka decouples producers from consumers and allows **multiple services to independently consume and replay events**.

---

## 2. Tech Stack

* Docker & Docker Compose
* Apache Kafka (Confluent image)
* Python 3
* kafka-python library

---

## 3. Prerequisites

Ensure the following are installed:

* Docker Desktop (running)
* Python 3.9+
* pip

Verify:

```bash
docker --version
python --version
```

---

## 4. Project Structure

```
.
├── docker-compose.yml
├── bank_txn_producer.py
├── market_price_producer.py
├── recommendation_consumer.py
└── README.md
```

---

## 5. Start Kafka

From the project root:

```bash
docker compose up -d
```

Verify containers:

```bash
docker ps
```

You should see:

* kafka-kafka-1
* kafka-zookeeper-1

---

## 6. Create Kafka Topics

Create the **bank transaction event stream**:

```bash
docker exec -it kafka-kafka-1 kafka-topics --create \
  --topic bank.transactions \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1
```

Create the **market price event stream**:

```bash
docker exec -it kafka-kafka-1 kafka-topics --create \
  --topic market.price.updates \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1
```

Verify topics:

```bash
docker exec -it kafka-kafka-1 kafka-topics --list --bootstrap-server localhost:9092
```

---

## 7. Install Python Dependencies

```bash
pip install kafka-python
```

---

## 8. Run the Application

### 8.1 Start Bank Transaction Producer

```bash
python bank_txn_producer.py
```

This simulates:

* New bank account transactions
* Events coming from bank APIs or ERP feeds

---

### 8.2 Start Market Price Producer

In a new terminal:

```bash
python market_price_producer.py
```

This simulates:

* Market instrument price changes
* Real-time market data updates

---

### 8.3 Start Recommendation Consumer

In another terminal:

```bash
python recommendation_consumer.py
```

This consumer:

* Subscribes to both event streams
* Reacts to each event
* Represents downstream workflows like recommendations or analytics

---

## 9. What You Will See

* Producers continuously publish events to Kafka
* Kafka stores events durably
* Consumer prints events as they are consumed
* Consumer logic reacts based on event type

This demonstrates:

* Asynchronous communication
* Loose coupling
* Real-time event processing

---

## 10. Event Replay Demo

To demonstrate **Kafka replay capability**:

1. Stop the consumer (`Ctrl + C`)
2. Restart the consumer

Kafka will re-deliver events from the beginning (based on configuration).

This is critical for:

* Audits
* Recomputing recommendations
* ML model retraining

---

## 11. Why Kafka (Design Rationale)

Kafka was chosen because it:

* Acts as a **system of record for events**
* Supports **multiple independent consumers**
* Allows **event replay**
* Scales for high-volume financial data
* Fits enterprise, compliance-heavy use cases

RabbitMQ may still be used for **internal task execution**, but Kafka is the backbone.

---

## 12. Next Steps (Out of Scope for This Skeleton)

* Schema Registry (Avro / JSON schema enforcement)
* Security (SASL / ACLs)
* Monitoring & metrics
* Stream processing (Kafka Streams / Flink)
* Production deployment (Managed Kafka)

---

## 13. Purpose of This Skeleton

This project is **not production-ready**.

It exists to:

* Validate architecture choice
* Educate stakeholders
* Provide a base for further development

---

## 14. Summary

This skeleton demonstrates how Capera can use Kafka as an **enterprise-wide event bus** to power:

* Investment recommendations
* Analytics
* Alerts
* ML pipelines

All built on a durable, scalable, and replayable event foundation.
