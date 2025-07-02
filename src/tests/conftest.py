from collections.abc import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient

from main import app


@pytest.fixture(scope='module')
async def async_client() -> AsyncGenerator[AsyncClient]:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
