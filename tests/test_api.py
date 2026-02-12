import pytest
import requests
from jsonschema import validate
from utils.mock_api import CONTACT_SCHEMA

@pytest.mark.should_have
def test_mock_api_contract(logger):
    response = requests.get("http://localhost:5000/mock/contact")
    validate(instance=response.json(), schema=CONTACT_SCHEMA)
    logger.info("Contract Validated")