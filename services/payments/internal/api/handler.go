package api

import (
	"encoding/json"
	"net/http"

	"github.com/mrarjona/synthetic-shop/services/payments/internal/gateway"
	"github.com/mrarjona/synthetic-shop/services/payments/internal/ledger"
)

func ChargeHandler(gw *gateway.Gateway, l *ledger.Ledger) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		var req ChargeRequest
		_ = json.NewDecoder(r.Body).Decode(&req)
		id, err := gw.Charge(req.Amount, req.Currency)
		if err != nil {
			http.Error(w, err.Error(), http.StatusBadGateway)
			return
		}
		l.Record(id, req.Amount)
		_ = json.NewEncoder(w).Encode(ChargeResponse{ID: id})
	}
}
