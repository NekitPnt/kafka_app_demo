import random
from datetime import datetime
from faker import Faker

from ingest_waves_demo.types import UploadData, MetaType, MetaGenre, MetaZodiac

fake: Faker = Faker()


def new_content():
    cont = UploadData()
    meta_class = random.choice([MetaType, MetaGenre, MetaZodiac])
    cont.meta = cont.meta.__dict__
    cont = cont.__dict__
    return cont
    {
        "s3_url": fake.url(),
        "meta": {
            "title": fake.catch_phrase(),
            "duration": fake.numerify(),
            "position": 1,
            "play_count": 0,
            random.choice(['type', 'genre', 'zodiac_sign']): fake.tld(),
            'date': fake.time(),
            'availability': fake.boolean(),
            'pdate': 0,
            'explicit': fake.boolean()
        }
    }


def get_content_from_s3(url: str):
    return fake.binary(128)


def save_content_to_s3(content):
    pass
