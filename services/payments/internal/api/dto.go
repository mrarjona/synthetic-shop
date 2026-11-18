package api

type ChargeRequest struct {
	Amount   int64  `json:"amount"`
	Currency string `json:"currency"`
}

type ChargeResponse struct {
	ID string `json:"id"`
}
