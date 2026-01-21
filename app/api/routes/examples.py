from fastapi import APIRouter

from app.api.dependencies import UOWDep
from app.api.schemas import CreateExampleIn
from app.business.usecases.create_example import CreateExample

router = APIRouter()


@router.post("/examples")
async def create_example(payload: CreateExampleIn, uow: UOWDep):
    usecase = CreateExample()
    new_id = await usecase.execute(uow=uow, name=payload.name)
    return {"id": str(new_id)}
