# AWS Kafka Real-Time Streaming Pipeline

Project Overview

This project demonstrates a real-time data streaming pipeline built on AWS using Apache Kafka. The pipeline ingests cryptocurrency price data from a public API and stores streaming events in an S3 data lake.

Architecture

API → Kafka Producer → Kafka Broker → Kafka Consumer → Amazon S3

Technologies Used

- AWS EC2
- Apache Kafka
- Python
- Amazon S3
- Boto3
- CoinGecko API

Pipeline Flow

1. Producer fetches cryptocurrency prices from the CoinGecko API.
2. Producer sends events to Kafka topic `crypto-prices`.
3. Kafka stores streaming events.
4. Consumer reads events from Kafka.
5. Consumer uploads events to Amazon S3 in partitioned format.

Example Event

json
{
  "timestamp": "2026-03-08T12:00:00",
  "source": "coingecko",
  "data": {
    "bitcoin": {"usd": 67000},
    "ethereum": {"usd": 1950}
  }
}

Steps:
Setup Steps - Launch EC2 instance - Install Java and Kafka - Start Zookeeper and Kafka - Create Kafka topic - Run producer - 
Run consumer - Verify files in S3

