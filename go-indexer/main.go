package main

import "fmt"

func main() {
	codeDir := "../../cobra"
	outputDir := "../output"

	fmt.Println("Parsing directory:", codeDir)
	functions := ParseFunctions(codeDir)
	for _, fn := range functions {
		hash := HashFunction(fn.Code)
		StoreCodeChunk(hash, fn.Code, outputDir)
		UpdateSummaryStub(fn.ID, hash, fn.Path, outputDir)
	}
	BuildSummaryTree(outputDir)
}
