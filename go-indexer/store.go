package main

import (
	"encoding/json"
	"path/filepath"
	"strings"
)

// TreeNode represents a node in the summary tree
type TreeNode struct {
	Name     string               `json:"name"`
	Type     string               `json:"type"` // "dir", "file", or "function"
	Children map[string]*TreeNode `json:"children,omitempty"`
	Data     map[string]string    `json:"data,omitempty"` // For function nodes
}

func StoreCodeChunk(hash, code, dir string) {
	path := filepath.Join(dir, "code_chunks", hash+".txt")
	WriteFile(path, code)
}

func UpdateSummaryStub(id, hash, file string, dir string) {
	stubPath := filepath.Join(dir, "summaries.json")
	stubs := LoadSummaries(stubPath)

	stubs[id] = map[string]string{
		"hash":    hash,
		"path":    file,
		"summary": "",
	}

	SaveSummaries(stubPath, stubs)
}

func BuildSummaryTree(dir string) {
	stubPath := filepath.Join(dir, "summaries.json")
	treePath := filepath.Join(dir, "tree.json")

	// Create root node
	root := &TreeNode{
		Name:     "root",
		Type:     "dir",
		Children: make(map[string]*TreeNode),
	}

	// Load summaries
	summaries := LoadSummaries(stubPath)

	// Build tree
	for id, data := range summaries {
		path := data["path"]
		parts := strings.Split(filepath.Clean(path), string(filepath.Separator))

		current := root
		// Build directory structure
		for i, part := range parts {
			if _, exists := current.Children[part]; !exists {
				nodeType := "dir"
				if i == len(parts)-1 {
					nodeType = "file"
				}
				current.Children[part] = &TreeNode{
					Name:     part,
					Type:     nodeType,
					Children: make(map[string]*TreeNode),
				}
			}
			current = current.Children[part]
		}

		// Add function node
		fnName := strings.TrimPrefix(id, data["hash"]+"_")
		current.Children[fnName] = &TreeNode{
			Name: fnName,
			Type: "function",
			Data: data,
		}
	}

	// Save tree
	treeData, err := json.MarshalIndent(root, "", "  ")
	if err != nil {
		panic(err)
	}
	WriteFile(treePath, string(treeData))
}
