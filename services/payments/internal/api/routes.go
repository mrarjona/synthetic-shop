package api

import (
	"net/http"

	"github.com/mrarjona/synthetic-shop/services/payments/internal/gateway"
	"github.com/mrarjona/synthetic-shop/services/payments/internal/ledger"
	"github.com/mrarjona/synthetic-shop/services/payments/internal/refunds"
)

func Routes(gw *gateway.Gateway, l *ledger.Ledger, r refunds.Refunder) http.Handler {
	mux := http.NewServeMux()
	mux.Handle("/charges", ChargeHandler(gw, l))
	mux.HandleFunc("/refunds", func(w http.ResponseWriter, req *http.Request) {
		id, err := refunds.Refund(r, l, req.URL.Query().Get("charge"), 100)
		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}
		_, _ = w.Write([]byte(id))
	})
	return mux
}
