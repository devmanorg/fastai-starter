import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_hello_endpoint(async_client: AsyncClient) -> None:
    response = await async_client.get("/hello-world")

    response_content = response.json()
    assert response.status_code == 200
    assert response_content["message"] == "Hello, FastAI!"
