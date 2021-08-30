def save_meta_to_db(meta: dict):
    print(f"Meta saved: {meta}")


def convert_upload_content_meta(meta: dict):
    return meta


def convert_meta_for_kafka_ingest(new_meta: dict):
    meta = {
        'availability': new_meta['availability'],
        'track_id': 1234,
        'duration': 4321,
        'format': 'mp3'
    }
    return meta
