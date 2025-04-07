# Smart Code Indexer

A tool that indexes and summarizes Go code functions, making codebases more searchable and understandable.

## Overview

This project consists of two main components:
1. A Go-based code indexer that extracts functions from Go source files
2. A Python-based summarizer that uses LLMs to generate function summaries

## Features

- Extracts functions from Go source files
- Generates unique hashes for each function
- Stores function code chunks efficiently
- Maintains a searchable index of functions
- Generates summaries using LLM (GPT-4)
- Optional hierarchical view of the codebase

## Project Structure

```
.
├── go-indexer/         # Go code indexer
│   ├── main.go        # Entry point
│   ├── parser.go      # Function parsing logic
│   ├── hasher.go      # Hash generation
│   ├── store.go       # Storage operations
│   └── utils.go       # Utility functions
├── python-summarizer/  # Python LLM summarizer
│   └── openai_client.py # OpenAI API integration
└── output/            # Generated output
    ├── code_chunks/   # Stored function code
    └── summaries.json # Function metadata and summaries
```

## Installation

1. Install Go 1.21 or later
2. Install Python 3.8 or later
3. Install dependencies:
   ```bash
   # Go dependencies
   cd go-indexer
   go mod tidy

   # Python dependencies
   cd ../python-summarizer
   pip install openai
   ```

## Usage

1. Set up your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

2. Run the indexer:
   ```bash
   cd go-indexer
   go run .
   ```

3. Generate summaries:
   ```bash
   cd ../python-summarizer
   python openai_client.py
   ```

## Output

- `code_chunks/`: Contains individual function code files
- `summaries.json`: Maps function IDs to their metadata and summaries
- `tree.json` (optional): Hierarchical view of the codebase

## Future Enhancements

- Vector embeddings for semantic search
- Git integration for automatic updates
- Query interface for finding relevant functions
- Caching system for LLM context

## License

MIT License
