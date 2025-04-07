package main

import (
	"encoding/json"
	"io/fs"
	"os"
	"path/filepath"
)

// GetGoFiles returns all .go files in the given directory and its subdirectories
func GetGoFiles(root string) []string {
	var files []string
	filepath.WalkDir(root, func(path string, d fs.DirEntry, err error) error {
		if err != nil {
			return err
		}
		if !d.IsDir() && filepath.Ext(path) == ".go" {
			files = append(files, path)
		}
		return nil
	})
	return files
}

// ReadFile reads the entire file and returns its contents as a string
func ReadFile(path string) string {
	content, err := os.ReadFile(path)
	if err != nil {
		// In production code, we should handle this error more gracefully
		panic(err)
	}
	return string(content)
}

// WriteFile writes data to a file, creating the file if it doesn't exist
func WriteFile(path string, data string) {
	dir := filepath.Dir(path)
	if err := os.MkdirAll(dir, 0755); err != nil {
		panic(err)
	}
	if err := os.WriteFile(path, []byte(data), 0644); err != nil {
		panic(err)
	}
}

// LoadSummaries loads the summaries from a JSON file
func LoadSummaries(path string) map[string]map[string]string {
	if _, err := os.Stat(path); os.IsNotExist(err) {
		return make(map[string]map[string]string)
	}

	data, err := os.ReadFile(path)
	if err != nil {
		panic(err)
	}

	var summaries map[string]map[string]string
	if err := json.Unmarshal(data, &summaries); err != nil {
		panic(err)
	}
	return summaries
}

// SaveSummaries saves the summaries to a JSON file
func SaveSummaries(path string, summaries map[string]map[string]string) {
	data, err := json.MarshalIndent(summaries, "", "  ")
	if err != nil {
		panic(err)
	}

	dir := filepath.Dir(path)
	if err := os.MkdirAll(dir, 0755); err != nil {
		panic(err)
	}

	if err := os.WriteFile(path, data, 0644); err != nil {
		panic(err)
	}
}

// GenerateID creates a unique identifier for a function based on its code and file path
func GenerateID(code string, filePath string) string {
	return HashFunction(code + filePath)
}
