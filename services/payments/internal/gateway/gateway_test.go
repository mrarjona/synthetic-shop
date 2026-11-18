package gateway

import "testing"

func TestCharge(t *testing.T) {
	if _, err := New(NewStripe()).Charge(100, "EUR"); err != nil {
		t.Fatal(err)
	}
}
