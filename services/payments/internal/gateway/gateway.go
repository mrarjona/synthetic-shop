package gateway

import "github.com/mrarjona/synthetic-shop/services/payments/internal/money"

type Provider interface {
	Charge(amount money.Cents, currency string) (string, error)
}

type Gateway struct{ provider Provider }

func New(p Provider) *Gateway { return &Gateway{provider: p} }

func (g *Gateway) Charge(amount int64, currency string) (string, error) {
	return withRetry(3, func() (string, error) { return g.provider.Charge(money.Cents(amount), currency) })
}
