from uuid import UUID

from app.business.uow import UnitOfWork


class CreateExample:
    async def execute(self, uow: UnitOfWork, name: str) -> UUID:
        async with uow:
            new_id = await uow.example.add(name=name)
            await uow.commit()
            return new_id
