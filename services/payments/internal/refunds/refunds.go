package refunds

import (
	"fmt"

	"github.com/mrarjona/synthetic-shop/services/payments/internal/ledger"
	"github.com/mrarjona/synthetic-shop/services/payments/internal/money"
)

type Refunder interface {
	Refund(chargeID string, amount money.Cents) (string, error)
}

func Refund(r Refunder, l *ledger.Ledger, chargeID string, amount int64) (string, error) {
	if amount <= 0 {
		return "", fmt.Errorf("refund amount must be positive")
	}
	id, err := r.Refund(chargeID, money.Cents(amount))
	if err == nil {
		l.Record(id, -amount)
	}
	return id, err
}
