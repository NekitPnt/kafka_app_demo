from kafka import KafkaConsumer
from json import loads


ingest_consumer = KafkaConsumer(
    'ingest',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-2',
    value_deserializer=lambda v: loads(v.decode('utf-8')),
    bootstrap_servers=['localhost:9092']
)


if __name__ == "__main__":
    for m in ingest_consumer:
        print(f"Ingest kafka meta: {m.value}")
