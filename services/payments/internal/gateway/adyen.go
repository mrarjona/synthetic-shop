package gateway

import (
	"fmt"

	"github.com/mrarjona/synthetic-shop/services/payments/internal/money"
)

type Adyen struct{}

func (a *Adyen) Charge(amount money.Cents, currency string) (string, error) {
	return fmt.Sprintf("psp_%d_%s", amount, currency), nil
}
