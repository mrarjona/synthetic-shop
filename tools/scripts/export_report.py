"""Export the orders table as SQL."""
from orders.repository.memory import ORDERS
from orders.repository.sql import save

for order in ORDERS.items.values():
    print(save(order))
