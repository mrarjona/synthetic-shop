"""Export the orders of a running orders service as CSV, through its HTTP API."""
import json
import urllib.request

with urllib.request.urlopen("http://localhost:8000/backoffice/orders") as r:
    for order_id in json.load(r):
        print(order_id)
