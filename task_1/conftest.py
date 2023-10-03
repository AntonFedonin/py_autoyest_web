import pytest


@pytest.fixture()
def valid_text():
    return 'молоко'


@pytest.fixture()
def invalid_text():
    return 'малоко'
