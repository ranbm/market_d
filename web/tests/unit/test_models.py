from web.market.models import Item, User

"""
user model values:


id = db.Column(db.Integer(), primary_key=True)
username = db.Column(db.String(length=30), nullable=False, unique=True)
email_address = db.Column(db.String(length=50), nullable=False, unique=True)
password_hash = db.Column(db.String(length=60), nullable=False)
budget = db.Column(db.Integer(), nullable=False, default=1000)
items = db.relationship("Item", backref="owned_user", lazy=True)


item model values:


id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey("user.id"))

"""


def test_new_user(new_user):
    assert new_user.email_address == "a@g.com"
    assert new_user.password_hash != "111111"


def test_new_item(new_item):
    assert new_item.name == "laptop"
    assert new_item.barcode == "124910457512"
    assert new_item.price == 1000
    assert new_item.description == "test"
    assert len(new_item.barcode) == 12
