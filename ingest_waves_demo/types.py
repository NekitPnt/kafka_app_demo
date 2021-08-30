import random
from dataclasses import dataclass
from typing import Union
from faker import Faker

fake: Faker = Faker()


@dataclass
class BaseMeta:
    title: str = fake.catch_phrase()
    duration: int = fake.numerify()
    position: int = 1
    play_count: int = 0
    date: str = fake.time()
    availability: bool = fake.boolean()
    pdate: int = 0
    explicit: bool = fake.boolean()


@dataclass
class MetaType(BaseMeta):
    type: str = fake.tld()


@dataclass
class MetaGenre(BaseMeta):
    genre: str = fake.tld()


@dataclass
class MetaZodiac(BaseMeta):
    zodiac_sign: str = fake.tld()


@dataclass
class UploadData:
    s3_url: str = Faker().url()
    meta: Union[MetaType, MetaGenre, MetaZodiac] = random.choice([MetaType(), MetaGenre(), MetaZodiac()])
