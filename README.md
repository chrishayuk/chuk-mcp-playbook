# Chuk MCP Playbook Server

A queryable playbook repository MCP server that stores executable knowledge as markdown and retrieves it via fast keyword search.

## Overview

This MCP server acts as a "Playbook Repository" that:
- **Ingests** markdown playbooks containing step-by-step instructions in plain English
- **Stores** them in-memory (with extensible storage via factory pattern)
- **Returns** LLM-friendly playbooks that can be fed directly to AI planners
- **Queries** using natural language for fast retrieval

## Architecture

Built with clean architecture principles:

```
src/chuk_mcp_playbook/
├── models/              # Pydantic domain models
│   └── playbook.py      # Playbook, PlaybookMetadata, PlaybookQuery
├── storage/             # Storage layer with factory pattern
│   ├── base.py          # Abstract PlaybookStorage interface
│   ├── factory.py       # StorageFactory and StorageType enum
│   └── providers/       # Storage implementations
│       └── memory.py    # In-memory storage (default)
├── services/            # Business logic
│   └── playbook_service.py  # PlaybookService
├── loader.py            # Markdown playbook loader
└── server.py            # MCP server with async tools
```

### Key Design Principles

- **Pydantic Native**: All models use Pydantic for type safety
- **Async Native**: All operations are async
- **No Magic Strings**: Type-safe enums and Pydantic models throughout
- **Factory Pattern**: Easy to add new storage providers (vector DB, SQL, etc.)
- **Clean Separation**: Models, storage, services, and server are properly separated

## Installation

```bash
# Clone or navigate to the repository
cd chuk-mcp-playbook

# Install dependencies
pip install -e .

# Or install from parent directory
pip install -e /Users/christopherhay/chris-source/chuk-ai/mcp-servers/chuk-mcp-server
pip install -e .
```

## Usage

### Running the Server

The server supports two transport modes:

**STDIO Mode (Default - for Claude Desktop, mcp-cli)**
```bash
# Using uv (recommended)
uv run chuk-mcp-playbook

# Or with explicit transport
uv run chuk-mcp-playbook --transport stdio

# Or activate venv first
source .venv/bin/activate
chuk-mcp-playbook
```

**HTTP Mode (for web/API access)**
```bash
# Using uv
uv run chuk-mcp-playbook http

# Or using make
make run-http
```

The server will automatically load all playbooks from the `playbooks/` directory on startup.

### Quick Test

Run the included test script to verify everything works:

```bash
python test_server.py
```

### MCP Tools

#### `query_playbook`
Query for a playbook using natural language.

```python
question: str  # e.g., "How do I get sunset times?"
top_k: int = 3  # Max results to return
→ Returns: Markdown content of the most relevant playbook
```

#### `ingest_playbook`
Add a new playbook to the repository.

```python
title: str
content: str  # Markdown content
description: str
tags: list[str] | None = None
author: str | None = None
→ Returns: Success message
```

#### `list_playbooks`
List all available playbooks.

```python
→ Returns: list[str]  # All playbook titles
```

#### `get_playbook`
Retrieve a specific playbook by exact title.

```python
title: str
→ Returns: Markdown content or error message
```

#### `get_stats`
Get repository statistics.

```python
→ Returns: {"total_playbooks": int}
```

## Examples

See the [`examples/`](examples/) directory for practical demonstrations:

- **01_basic_query.py** - Basic querying and retrieval
- **02_ingest_playbook.py** - Creating and adding playbooks programmatically
- **03_async_api_usage.py** - Concurrent operations and performance
- **04_custom_storage.py** - Building custom storage providers
- **05_mcp_client_simulation.py** - AI planner integration workflow

Run all examples:
```bash
source .venv/bin/activate
cd examples
./run_all.sh
```

## Playbook Format

Playbooks are markdown files with a specific structure designed for LLM consumption:

```markdown
# Playbook: [Title]

## Description
Brief description of what this playbook does

## Prerequisites
- Required inputs or conditions

## Steps

1. First step in plain English
2. Second step with clear instructions
3. Continue with all necessary steps

## MCP Tools Required

### server-name
- **Tool**: `tool_name`
- **Parameters**:
  - `param1` (type): Description
  - `param2` (type): Description

## Example Usage

**Input**: Example user question

**Process**:
1. Step breakdown
2. ...

**Output**:
```
Expected result
```

## Expected Response Format

Format for the final output

## Error Handling

- Common errors and how to handle them

## Notes

- Additional helpful information
```

## Example Playbooks

Three weather-related playbooks are included:

1. **Get Sunset and Sunrise Times**: Retrieve sunrise/sunset for a location
2. **Get Weather Forecast**: Multi-day weather forecast
3. **Get Current Weather Conditions**: Real-time weather data

All use the `chuk-mcp-open-meteo` server.

## Integration with AI Planner

The playbooks are designed to work with `chuk-ai-planner`:

1. LLM asks: "How do I get sunset times?"
2. Planner calls: `query_playbook(question="sunset times")`
3. Server returns: Full playbook with steps in English
4. Planner parses the playbook and creates a sub-plan
5. Planner executes the steps using the specified MCP tools

## Extending Storage

To add a new storage provider:

1. Create a new provider in `storage/providers/`:

```python
from chuk_mcp_playbook.storage.base import PlaybookStorage

class MyStorage(PlaybookStorage):
    async def add_playbook(self, playbook: Playbook) -> None:
        # Implementation
        pass

    # Implement all abstract methods...
```

2. Add to factory in `storage/factory.py`:

```python
class StorageType(str, Enum):
    MEMORY = "memory"
    MY_STORAGE = "my_storage"  # Add new type

class StorageFactory:
    @staticmethod
    def create(storage_type: StorageType, **kwargs):
        if storage_type == StorageType.MY_STORAGE:
            return MyStorage(**kwargs)
        # ...
```

## Future Enhancements

- **Vector Storage**: Add ChromaDB/LanceDB provider for semantic search
- **Persistent Storage**: SQLite/PostgreSQL providers
- **Playbook Versioning**: Track changes over time
- **Templates**: Playbook templates for common patterns
- **Validation**: Schema validation for playbook structure
- **REST API**: HTTP endpoint for web integration

## Performance

- **In-Memory Search**: Sub-millisecond query times
- **Startup**: Loads all playbooks in < 100ms
- **Async**: Non-blocking operations throughout
- **Scalable**: Factory pattern ready for high-performance backends

## License

MIT
