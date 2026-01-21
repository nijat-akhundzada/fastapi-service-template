from typing import Annotated

from fastapi import Depends

from app.business.uow import UnitOfWork
from app.data.uow_sql import SqlAlchemyUnitOfWork


async def get_uow() -> UnitOfWork:
    return SqlAlchemyUnitOfWork()


UOWDep = Annotated[UnitOfWork, Depends(get_uow)]
