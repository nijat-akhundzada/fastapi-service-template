from sqlalchemy.ext.asyncio import AsyncSession

from app.business.uow import UnitOfWork
from app.data.db import SessionLocal
from app.data.repositories_sql import ExampleRepoSQL


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self):
        self.session: AsyncSession | None = None
        self.example = None
        self._committed = False

    async def __aenter__(self):
        self.session = SessionLocal()
        self.example = ExampleRepoSQL(self.session)
        self._committed = False
        return self

    async def __aexit__(self, exc_type, exc, tb):
        try:
            # rollback on any exception OR if user forgot to commit
            if exc_type or not self._committed:
                await self.rollback()
        finally:
            if self.session:
                await self.session.close()

    async def commit(self) -> None:
        assert self.session is not None
        await self.session.commit()
        self._committed = True

    async def rollback(self) -> None:
        assert self.session is not None
        await self.session.rollback()
