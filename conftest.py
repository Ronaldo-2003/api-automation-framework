import pytest
from core.client import APIClient


@pytest.fixture(scope="session")
def api_client():
    return APIClient()
