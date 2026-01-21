from uuid import UUID, uuid4

import pytest

from app.api.dependencies import get_uow
from app.business.uow import UnitOfWork


class MockExampleRepo:
    def __init__(self):
        self.items = []

    async def add(self, name: str) -> UUID:
        new_id = uuid4()
        self.items.append({"id": new_id, "name": name})
        return new_id

    async def count(self) -> int:
        return len(self.items)


class MockUOW(UnitOfWork):
    def __init__(self):
        self.example = MockExampleRepo()
        self.committed = False

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def commit(self) -> None:
        self.committed = True

    async def rollback(self) -> None:
        pass


@pytest.mark.asyncio
async def test_create_example(app, client):
    mock_uow = MockUOW()
    app.dependency_overrides[get_uow] = lambda: mock_uow

    try:
        response = await client.post("/api/v1/examples", json={"name": "test item"})
        assert response.status_code == 200

        data = response.json()
        assert "id" in data
        UUID(data["id"])  # validates UUID format

        assert len(mock_uow.example.items) == 1
        assert mock_uow.example.items[0]["name"] == "test item"
        assert mock_uow.committed is True
    finally:
        app.dependency_overrides.clear()
