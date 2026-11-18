package ledger

import "testing"

func TestRecord(t *testing.T) {
	s := NewMemoryStore()
	New(s).Record("x", 1)
	if len(s.entries) != 1 {
		t.Fatal("not recorded")
	}
}
