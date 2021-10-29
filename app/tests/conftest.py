import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture
def test_client():
    with TestClient(app) as client:
        yield client


@pytest.fixture
def test_data():
    data = {"date": "31.01.2021", "periods": 7, "amount": 10000, "rate": 6.00}
    return data


@pytest.fixture
def test_bad_data():
    data = {
        "date": "31.01.2021",
        "periods": 7,
    }
    return data


@pytest.fixture
def test_not_validate_date():
    data = {"date": "31/01/2021", "periods": 7, "amount": 10000, "rate": 6.00}
    return data


@pytest.fixture
def test_not_validate_periods():
    data = {"date": "31.01.2021", "periods": 61, "amount": 10000, "rate": 6.00}
    return data


@pytest.fixture
def test_not_validate_amount():
    data = {"date": "31.01.2021", "periods": 8, "amount": 1000, "rate": 6.00}
    return data


@pytest.fixture
def test_not_validate_rate():
    data = {"date": "31.01.2021", "periods": 8, "amount": 10000, "rate": 9}
    return data
