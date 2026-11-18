"""Seed a running orders service with demo orders through its HTTP API."""
import json
import urllib.request
from decimal import Decimal

from shopcore.money import Money

for i in range(10):
    body = {"customer": f"c{i}@example.com", "items": [{"sku": "sku-1", "quantity": 1,
            "unit_price": str(Money(Decimal(i)).amount)}]}
    req = urllib.request.Request("http://localhost:8000/checkout", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    urllib.request.urlopen(req)
