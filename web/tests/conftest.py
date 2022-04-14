import pytest

from web.market import app
from web.market.models import Item, User


@pytest.fixture
def new_user():
    user = User(username="abc", email_address="a@g.com", password="111111")
    return user


@pytest.fixture
def new_item():
    item = Item(name="laptop", price=1000, barcode="124910457512", description="test")
    return item


@pytest.fixture
def test_client():
    with app.test_client() as testing_client:
        yield testing_client
