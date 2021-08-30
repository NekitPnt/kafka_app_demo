import random
from datetime import datetime
from faker import Faker

from ingest_waves_demo.types import UploadData, MetaType, MetaGenre, MetaZodiac

fake: Faker = Faker()


def new_content():
    meta_class = random.choice([MetaType, MetaGenre, MetaZodiac])
    meta = meta_class(
        fake.catch_phrase(),
        fake.numerify(),
        1,
        0,
        fake.time(),
        fake.boolean(),
        0,
        fake.boolean(),
        fake.tld()
    )
    cont = UploadData(fake.url(), meta)
    cont.meta = cont.meta.__dict__
    cont = cont.__dict__
    return cont


def get_content_from_s3(url: str):
    return fake.binary(128)


def save_content_to_s3(content):
    print(f"File saved: {content}")
