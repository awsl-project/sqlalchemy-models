from typing import Dict
from pydantic import BaseModel


class Blob(BaseModel):
    url: str
    width: int
    height: int


class Blobs(BaseModel):
    blobs: Dict[str, Blob]


class BlobGroup(BaseModel):
    id: str
    awsl_id: str
    blobs: Blobs
