from kafka import KafkaConsumer, KafkaProducer
from json import loads, dumps

from ingest_waves_demo.repositories import content, meta

import logging

# logging.basicConfig(level=logging.INFO)

upload_consumer = KafkaConsumer(
    'upload',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-1',
    value_deserializer=lambda v: loads(v.decode('utf-8')),
    bootstrap_servers=['localhost:9092']
)

ingest_producer = KafkaProducer(
    value_serializer=lambda v: dumps(v).encode('utf-8'),
    retries=5,
    request_timeout_ms=2000,
    bootstrap_servers='localhost:9092',
    api_version=(2, 5, 0)
)


if __name__ == "__main__":
    for m in upload_consumer:
        # 1) Получать файл контента из хранилища S3 по пути из сообщения
        binary_content = content.get_content_from_s3(m.value['s3_url'])
        # 2) Сохраняться файл в S3 хранилище обработанного контента
        content.save_content_to_s3(binary_content)
        # 3) Сохранять метаданные трека контента в БД meta в таблице track, со следующими значениями:
        new_meta = meta.convert_upload_content_meta(m.value['meta'])
        meta.save_meta_to_db(new_meta)
        # 4) Отправлять в kafka в топик ingest сообщение о сохранении нового файла c:
        ingest_kafka_meta = meta.convert_meta_for_kafka_ingest(new_meta)
        ingest_producer.send('ingest', ingest_kafka_meta).get()
        print(f"Ingest kafka meta: {ingest_kafka_meta}")
