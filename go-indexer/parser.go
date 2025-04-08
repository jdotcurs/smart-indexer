package main

import (
	"go/ast"
	"go/parser"
	"go/token"
	"os"
)

type Function struct {
	ID   string
	Code string
	Path string
}

func ParseFunctions(root string) []Function {
	var functions []Function
	files := GetGoFiles(root)

	for _, file := range files {
		src, err := os.ReadFile(file)
		if err != nil {
			continue // optionally log error
		}

		fset := token.NewFileSet()
		node, err := parser.ParseFile(fset, file, src, parser.AllErrors)
		if err != nil {
			continue
		}

		ast.Inspect(node, func(n ast.Node) bool {
			fn, ok := n.(*ast.FuncDecl)
			if ok && fn.Body != nil {
				start := fset.Position(fn.Pos()).Offset
				end := fset.Position(fn.End()).Offset
				code := string(src[start:end])
				id := GenerateID(code, file)
				functions = append(functions, Function{
					ID:   id,
					Code: code,
					Path: file,
				})
			}
			return true
		})
	}

	return functions
}
