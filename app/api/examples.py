from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.business.usecases.create_example import CreateExample
from app.data.uow_sql import SqlAlchemyUnitOfWork

router = APIRouter()


class CreateExampleIn(BaseModel):
    name: str = Field(min_length=1, max_length=200)


@router.post("/examples")
async def create_example(payload: CreateExampleIn):
    uow = SqlAlchemyUnitOfWork()
    usecase = CreateExample()
    new_id = await usecase.execute(uow=uow, name=payload.name)
    return {"id": str(new_id)}
