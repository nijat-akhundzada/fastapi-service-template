from abc import ABC, abstractmethod

from .repositories import ExampleRepository


class UnitOfWork(ABC):
    example: ExampleRepository

    @abstractmethod
    async def __aenter__(self): ...
    @abstractmethod
    async def __aexit__(self, exc_type, exc, tb): ...

    @abstractmethod
    async def commit(self) -> None: ...
    @abstractmethod
    async def rollback(self) -> None: ...
