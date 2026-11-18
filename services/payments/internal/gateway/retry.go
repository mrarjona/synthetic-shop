package gateway

func withRetry(times int, f func() (string, error)) (string, error) {
	var err error
	for i := 0; i < times; i++ {
		var id string
		if id, err = f(); err == nil {
			return id, nil
		}
	}
	return "", err
}
