package main

import (
	"log"
	"net/http"

	"github.com/mrarjona/synthetic-shop/services/payments/internal/api"
	"github.com/mrarjona/synthetic-shop/services/payments/internal/gateway"
	"github.com/mrarjona/synthetic-shop/services/payments/internal/ledger"
)

func main() {
	stripe := gateway.NewStripe()
	gw := gateway.New(stripe)
	l := ledger.New(ledger.NewMemoryStore())
	log.Fatal(http.ListenAndServe(":8080", api.Routes(gw, l, stripe)))
}
