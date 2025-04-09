package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
)

func main() {
	// Use current directory as default code directory if not specified
	codeDir := "."
	if len(os.Args) > 1 {
		codeDir = os.Args[1]
	}

	// Create output directory in the project root
	outputDir := "output"
	if err := os.MkdirAll(outputDir, 0755); err != nil {
		log.Fatalf("Failed to create output directory: %v", err)
	}

	// Create code_chunks directory
	chunksDir := filepath.Join(outputDir, "code_chunks")
	if err := os.MkdirAll(chunksDir, 0755); err != nil {
		log.Fatalf("Failed to create code chunks directory: %v", err)
	}

	fmt.Printf("📂 Parsing directory: %s\n", codeDir)
	functions := ParseFunctions(codeDir)
	fmt.Printf("Found %d functions\n", len(functions))

	for i, fn := range functions {
		hash := HashFunction(fn.Code)
		fmt.Printf("Processing function %d/%d: ID=%s\n", i+1, len(functions), fn.ID)

		StoreCodeChunk(hash, fn.Code, outputDir)
		UpdateSummaryStub(fn.ID, hash, fn.Path, outputDir)
	}

	fmt.Println("Building summary tree...")
	BuildSummaryTree(outputDir)
	fmt.Println("✅ Done! Check the output directory for results.")
}
