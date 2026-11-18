import os

DATABASE_URL = os.environ.get("ORDERS_DATABASE_URL", "sqlite:///orders.db")
DEFAULT_COUNTRY = os.environ.get("ORDERS_DEFAULT_COUNTRY", "ES")
