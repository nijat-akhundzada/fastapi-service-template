from typing import Protocol
from uuid import UUID


class ExampleRepository(Protocol):
    async def add(self, name: str) -> UUID: ...
    async def count(self) -> int: ...
