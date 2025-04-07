package main

func main() {
	codeDir := "./your-codebase"
	outputDir := "./output"

	functions := ParseFunctions(codeDir)
	for _, fn := range functions {
		hash := HashFunction(fn.Code)
		StoreCodeChunk(hash, fn.Code, outputDir)
		UpdateSummaryStub(fn.ID, hash, fn.Path, outputDir)
	}
	BuildSummaryTree(outputDir)
}
