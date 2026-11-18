package ledger

type Ledger struct{ store Store }

func New(s Store) *Ledger { return &Ledger{store: s} }

func (l *Ledger) Record(id string, amount int64) { l.store.Append(Entry{ID: id, Amount: amount}) }
