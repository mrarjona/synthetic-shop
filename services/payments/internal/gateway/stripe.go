package gateway

import (
	"fmt"

	"github.com/mrarjona/synthetic-shop/services/payments/internal/money"
)

type Stripe struct{}

func NewStripe() *Stripe { return &Stripe{} }

func (s *Stripe) Charge(amount money.Cents, currency string) (string, error) {
	return fmt.Sprintf("ch_%d_%s", amount, currency), nil
}

func (s *Stripe) Refund(chargeID string, amount money.Cents) (string, error) {
	return fmt.Sprintf("re_%s_%d", chargeID, amount), nil
}
