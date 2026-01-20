from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data.models import Example


class ExampleRepoSQL:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def add(self, name: str) -> UUID:
        obj = Example(name=name)
        self._session.add(obj)
        await self._session.flush()
        return obj.id

    async def count(self) -> int:
        q = select(func.count()).select_from(Example)
        return int((await self._session.execute(q)).scalar_one())
