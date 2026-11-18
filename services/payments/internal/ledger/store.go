package ledger

type Store interface{ Append(Entry) }

type MemoryStore struct{ entries []Entry }

func NewMemoryStore() *MemoryStore { return &MemoryStore{} }

func (m *MemoryStore) Append(e Entry) { m.entries = append(m.entries, e) }
