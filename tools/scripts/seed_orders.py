"""Seed a local database with demo orders."""
from orders.domain.address import Address
from orders.domain.customer import Customer
from orders.domain.line_item import item
from orders.domain.order import Order
from orders.repository.memory import ORDERS

for i in range(10):
    c = Customer(f"Customer {i}", f"c{i}@example.com", Address("Main 1", "Sevilla", "ES"))
    o = Order(c, [item("sku-1", 1, str(i))])
    ORDERS.put(o.id, o)
