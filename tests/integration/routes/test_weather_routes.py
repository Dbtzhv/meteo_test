import pytest
from httpx import AsyncClient
from starlette import status


@pytest.mark.asyncio
async def test_read_root(ac: AsyncClient):
    response = await ac.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert '<html lang="en">' in response.text
