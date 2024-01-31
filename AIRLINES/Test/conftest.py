import pytest  
from rest_framework.test import APIClient  
from typing import Iterator  
  
@pytest.fixture(scope="function")  
def api_client() -> Iterator[APIClient]:
    """  
    Fixture to provide an API client  
    :return: APIClient  
    """  
    yield APIClient()