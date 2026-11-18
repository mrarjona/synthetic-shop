package api

import (
	"net/http"

	"github.com/mrarjona/synthetic-shop/services/payments/internal/gateway"
	"github.com/mrarjona/synthetic-shop/services/payments/internal/ledger"
)

func Routes(gw *gateway.Gateway, l *ledger.Ledger) http.Handler {
	mux := http.NewServeMux()
	mux.Handle("/charges", ChargeHandler(gw, l))
	return mux
}
