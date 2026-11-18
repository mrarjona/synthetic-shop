from orders.domain.customer import Customer
from orders.repository.base import Repository


class CustomersRepository(Repository[Customer]):
    pass
