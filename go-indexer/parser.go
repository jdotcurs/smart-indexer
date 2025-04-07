package main

import "strings"

type Function struct {
	ID   string
	Code string
	Path string
}

func ParseFunctions(path string) []Function {
	// VERY basic: reads .go files and splits on "func"
	// In real version, use Go parser for AST-level accuracy
	var functions []Function
	files := GetGoFiles(path)
	for _, file := range files {
		content := ReadFile(file)
		parts := strings.Split(content, "func ")
		for i, part := range parts {
			if i == 0 {
				continue
			}
			snippet := "func " + part
			id := GenerateID(snippet, file)
			functions = append(functions, Function{ID: id, Code: snippet, Path: file})
		}
	}
	return functions
}
