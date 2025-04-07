package main

import (
	"crypto/sha256"
	"encoding/hex"
)

func HashFunction(code string) string {
	sum := sha256.Sum256([]byte(code))
	return hex.EncodeToString(sum[:])
}
