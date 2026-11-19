package refunds

import "testing"

func TestRejectsZero(t *testing.T) {
	if _, err := Refund(nil, nil, "ch_1", 0); err == nil {
		t.Fatal("expected an error")
	}
}
