from pydantic import BaseModel, Field


class CreateExampleIn(BaseModel):
    name: str = Field(min_length=1, max_length=200)


class ExampleOut(BaseModel):
    id: str
    name: str
