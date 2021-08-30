import time
import random
from kafka import KafkaProducer
from json import dumps
from repositories import content

import logging

logging.basicConfig(level=logging.INFO)


upload_producer = KafkaProducer(
    value_serializer=lambda m: dumps(m).encode('utf-8'),
    retries=5,
    request_timeout_ms=2000,
    bootstrap_servers='localhost:9092',
    api_version=(2, 5, 0)
)


if __name__ == "__main__":
    while True:
        new_content_data = content.new_content()
        upload_producer.send('upload', new_content_data).get()
        time.sleep(random.randint(1, 5))
