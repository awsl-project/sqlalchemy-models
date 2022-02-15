from typing import Dict, Union
from pydantic import BaseModel


class Blob(BaseModel):
    url: str
    width: Union[int, None]
    height: Union[int, None]


class Blobs(BaseModel):
    blobs: Dict[str, Blob]


class BlobGroup(BaseModel):
    id: str
    awsl_id: str
    blobs: Blobs
