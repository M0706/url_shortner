from pydantic import BaseModel, Field

class ShortURLModel(BaseModel):
    url: str

class LongURLModel(BaseModel):
    url: str