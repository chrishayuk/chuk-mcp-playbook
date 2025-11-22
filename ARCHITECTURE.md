# Architecture Overview

## Design Philosophy

This project follows **clean architecture** principles with a focus on:

1. **Pydantic Native**: All models use Pydantic for runtime type validation
2. **Async Native**: All I/O operations are async from the ground up
3. **No Magic Strings**: Type-safe enums and strongly-typed models
4. **Factory Pattern**: Pluggable storage backends
5. **Separation of Concerns**: Clear boundaries between layers

## Layer Architecture

```
┌─────────────────────────────────────────────┐
│           MCP Server (server.py)            │
│  - Exposes async MCP tools                  │
│  - Handles tool registration                │
│  - Manages server lifecycle                 │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│      Service Layer (services/)              │
│  - PlaybookService: Business logic          │
│  - Orchestrates storage operations          │
│  - Validates inputs                         │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│      Storage Layer (storage/)               │
│  - Abstract base: PlaybookStorage           │
│  - Factory: Creates storage providers       │
│  - Providers: Concrete implementations      │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│      Domain Models (models/)                │
│  - Playbook: Core entity                    │
│  - PlaybookMetadata: Metadata schema        │
│  - PlaybookQuery: Query parameters          │
└─────────────────────────────────────────────┘
```

## Directory Structure

```
src/chuk_mcp_playbook/
├── models/                    # Domain models (Pydantic)
│   ├── __init__.py
│   └── playbook.py           # Playbook, PlaybookMetadata, PlaybookQuery
│
├── storage/                   # Storage abstraction
│   ├── __init__.py
│   ├── base.py               # Abstract PlaybookStorage interface
│   ├── factory.py            # StorageFactory + StorageType enum
│   └── providers/            # Concrete storage implementations
│       ├── __init__.py
│       └── memory.py         # In-memory provider (default)
│
├── services/                  # Business logic layer
│   ├── __init__.py
│   └── playbook_service.py   # PlaybookService
│
├── loader.py                  # Markdown playbook loader
├── server.py                  # MCP server + tools
└── __init__.py               # Public API exports
```

## Key Components

### 1. Models (`models/playbook.py`)

**PlaybookMetadata** (Pydantic model)
- `title: str` - Playbook title
- `description: str` - Brief description
- `tags: list[str]` - Categorization tags
- `author: Optional[str]` - Author name
- `created_at: datetime` - Creation timestamp
- `updated_at: datetime` - Last update timestamp

**Playbook** (Pydantic model)
- `metadata: PlaybookMetadata` - Metadata object
- `content: str` - Full markdown content
- `matches_query(query: str) -> (bool, float)` - Query matching logic

**PlaybookQuery** (Pydantic model)
- `question: str` - Natural language query
- `top_k: int` - Max results (1-10)
- `tags: Optional[list[str]]` - Tag filter

### 2. Storage Layer (`storage/`)

**PlaybookStorage** (ABC)
- Abstract interface defining storage contract
- All methods are async
- Implementations must provide:
  - `add_playbook(playbook: Playbook)`
  - `get_playbook(title: str)`
  - `query(question, top_k, tags)`
  - `list_all()`
  - `delete_playbook(title)`
  - `clear()`
  - `count()`

**StorageFactory**
- Creates storage instances based on `StorageType` enum
- Extensible: easy to add new providers
- Current providers: `MEMORY`

**InMemoryStorage** (Provider)
- Fast dictionary-based storage
- Keyword matching with scoring
- O(n) search (acceptable for small datasets)
- Thread-safe for async operations

### 3. Service Layer (`services/playbook_service.py`)

**PlaybookService**
- Wraps storage with business logic
- Handles playbook creation with metadata
- Provides query interface
- Returns statistics

Key methods:
- `async create_playbook(...) -> Playbook`
- `async get_playbook(title) -> Optional[Playbook]`
- `async query_playbooks(question, top_k, tags) -> list[Playbook]`
- `async list_playbooks() -> list[str]`
- `async delete_playbook(title) -> bool`
- `async get_stats() -> dict`

### 4. Loader (`loader.py`)

**PlaybookLoader**
- Loads markdown files into storage
- Extracts metadata from markdown structure
- Auto-generates tags from filename
- Handles directories of playbooks

**load_default_playbooks**
- Convenience function to load from `playbooks/` dir
- Called on server startup
- Returns count of loaded playbooks

### 5. MCP Server (`server.py`)

**MCP Tools** (all async):

1. `query_playbook(question, top_k=3) -> str`
   - Natural language query
   - Returns markdown of top result

2. `ingest_playbook(title, content, description, tags, author) -> str`
   - Add new playbook
   - Returns success message

3. `list_playbooks() -> list[str]`
   - Get all playbook titles

4. `get_playbook(title) -> str`
   - Get specific playbook by exact title

5. `get_stats() -> dict`
   - Repository statistics

**Lifecycle Hooks**:
- `@mcp.on_startup`: Loads default playbooks

## Data Flow

### Query Flow
```
User Question
    ↓
query_playbook(question="How to get sunset?")
    ↓
PlaybookService.query_playbooks(question, top_k)
    ↓
InMemoryStorage.query(question, top_k, tags)
    ↓
For each playbook: playbook.matches_query(question)
    ↓
Sort by score, return top_k
    ↓
Return top result's markdown content to LLM
```

### Ingest Flow
```
Markdown file(s)
    ↓
PlaybookLoader.load_from_directory()
    ↓
Extract metadata from markdown
    ↓
PlaybookService.create_playbook(...)
    ↓
Create Playbook + PlaybookMetadata (Pydantic validation)
    ↓
InMemoryStorage.add_playbook(playbook)
    ↓
Store in dict[title, Playbook]
```

## Extensibility

### Adding a New Storage Provider

1. Create provider class:
```python
# storage/providers/my_provider.py
from chuk_mcp_playbook.storage.base import PlaybookStorage

class MyStorage(PlaybookStorage):
    async def add_playbook(self, playbook: Playbook) -> None:
        # Implementation
        pass

    # Implement all abstract methods...
```

2. Add to factory:
```python
# storage/factory.py
class StorageType(str, Enum):
    MEMORY = "memory"
    MY_STORAGE = "my_storage"  # Add new

class StorageFactory:
    @staticmethod
    def create(storage_type: StorageType, **kwargs):
        if storage_type == StorageType.MY_STORAGE:
            return MyStorage(**kwargs)
        # ...
```

3. Use it:
```python
storage = StorageFactory.create(StorageType.MY_STORAGE, ...)
```

## Performance Characteristics

### Current (In-Memory)
- **Query Time**: O(n) where n = number of playbooks
- **Storage**: O(n) memory
- **Startup**: O(n) to load playbooks
- **Throughput**: ~10,000 queries/sec (small dataset)

### Future Optimizations
- **Vector DB**: O(log n) query with semantic search
- **SQLite FTS**: O(log n) with full-text search index
- **Caching**: LRU cache for frequent queries

## Type Safety

All data flows through Pydantic models:
```python
# Input validation
PlaybookQuery(question="test", top_k=5)  # ✓ Valid
PlaybookQuery(question="test", top_k=20) # ✗ ValidationError (max 10)

# Output validation
playbook = Playbook(metadata=..., content=...)  # ✓ Validated
playbook.metadata.title  # ✓ Guaranteed to exist
```

## Testing Strategy

- **Unit tests**: Test individual components (models, storage, service)
- **Integration tests**: Test loader + service interaction
- **End-to-end tests**: Load playbooks, query, verify results
- All tests use async/await
- No mocking: use real in-memory storage for speed

## Future Enhancements

1. **Vector Search**: ChromaDB/LanceDB provider for semantic queries
2. **Persistent Storage**: SQLite/PostgreSQL providers
3. **Caching Layer**: Redis for frequent queries
4. **Versioning**: Track playbook changes over time
5. **Templates**: Reusable playbook templates
6. **Validation**: JSON schema validation for playbook structure
7. **REST API**: HTTP endpoints alongside MCP
