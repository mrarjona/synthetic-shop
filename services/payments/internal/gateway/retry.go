package gateway

import (
	"errors"
	"time"
)

// ErrPermanent marks a failure that retrying cannot fix (a declined card).
var ErrPermanent = errors.New("permanent failure")

func withRetry(times int, f func() (string, error)) (string, error) {
	return withBackoff(times, 0, f)
}

// withBackoff retries f, waiting longer after each failure, and stops at once on a permanent failure.
func withBackoff(times int, wait time.Duration, f func() (string, error)) (string, error) {
	var err error
	for i := 0; i < times; i++ {
		var id string
		if id, err = f(); err == nil {
			return id, nil
		}
		if errors.Is(err, ErrPermanent) {
			return "", err
		}
		if wait > 0 && i < times-1 {
			time.Sleep(wait * time.Duration(1<<i)) // TODO: add jitter
		}
	}
	return "", err
}
