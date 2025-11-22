# Chuk MCP Playbook Server - Examples

This directory contains practical examples demonstrating how to use the Chuk MCP Playbook Server programmatically.

## Prerequisites

Make sure you have installed the package:

```bash
cd ..
uv venv
source .venv/bin/activate
uv pip install -e .
```

## Running Examples

All examples are standalone Python scripts:

```bash
# From the examples directory
python 01_basic_query.py
python 02_ingest_playbook.py
python 03_async_api_usage.py
python 04_custom_storage.py
python 05_mcp_client_simulation.py

# Or from project root
python examples/01_basic_query.py
```

## Examples Overview

### 01_basic_query.py - Basic Query Operations

**What it demonstrates:**
- Creating a playbook service with in-memory storage
- Loading playbooks from the `playbooks/` directory
- Querying playbooks with natural language
- Retrieving specific playbooks by title
- Getting repository statistics

**Key concepts:**
- StorageFactory pattern
- PlaybookService usage
- Async operations
- Query scoring and ranking

**Sample output:**
```
📦 Creating in-memory storage...
✅ Storage created

📚 Loading playbooks...
✅ Loaded 3 playbooks

📋 Available playbooks:
  1. Get Current Weather Conditions
  2. Get Sunset and Sunrise Times
  3. Get Weather Forecast

🔍 Query: 'How do I get sunset times?'
✅ Found: Get Sunset and Sunrise Times
```

### 02_ingest_playbook.py - Creating & Adding Playbooks

**What it demonstrates:**
- Creating playbooks programmatically
- Ingesting new playbooks into storage
- Querying for newly added playbooks
- Working with playbook metadata (tags, author, etc.)

**Key concepts:**
- Playbook creation
- Metadata management
- Dynamic content addition
- Tag-based organization

**Use cases:**
- Adding playbooks at runtime
- Building playbook repositories dynamically
- User-generated playbooks
- API-driven playbook management

### 03_async_api_usage.py - Asynchronous Operations

**What it demonstrates:**
- Sequential vs concurrent query execution
- Performance benefits of async operations
- Running mixed operation types concurrently
- Error handling with asyncio.gather()

**Key concepts:**
- Async/await patterns
- Concurrent execution with asyncio.gather()
- Performance measurement
- Batch operations

**Sample output:**
```
🔄 Running 5 queries SEQUENTIALLY...
✅ Sequential execution completed in 2.45ms

⚡ Running 5 queries CONCURRENTLY...
✅ Concurrent execution completed in 0.89ms

📊 Performance Comparison:
   Sequential: 2.45ms
   Concurrent: 0.89ms
   Speedup: 2.75x faster
```

### 04_custom_storage.py - Extending Storage Layer

**What it demonstrates:**
- Creating custom storage providers
- Implementing the PlaybookStorage interface
- Wrapping existing providers to add functionality
- Combining multiple storage providers

**Custom providers shown:**
1. **LoggingStorage** - Logs all storage operations
2. **CachedStorage** - Adds caching for frequent reads
3. **Combined** - Logging + Caching together

**Key concepts:**
- Interface implementation
- Decorator/wrapper pattern
- Storage extensibility
- Performance optimization

**Use cases:**
- Adding logging/monitoring
- Implementing caching strategies
- Adding metrics collection
- Creating storage middleware

### 05_mcp_client_simulation.py - AI Planner Integration

**What it demonstrates:**
- How an AI planner would query playbooks
- Parsing playbook markdown structure
- Extracting steps and MCP tools
- Simulating playbook execution workflow

**Simulated workflow:**
1. User asks a question
2. Planner queries playbook repository
3. Playbook is returned as markdown
4. Planner parses steps and MCP tools
5. Planner creates execution plan
6. MCP tools are called with extracted parameters
7. Results are formatted and returned

**Key concepts:**
- Natural language → playbook mapping
- Markdown parsing
- Step extraction
- MCP tool identification
- Parameter extraction

**Sample output:**
```
🎯 User Question: 'What time is sunset in London today?'

📖 Parsing playbook...
✅ Found 6 sections

📝 Extracting steps...
  1. Determine the location coordinates
  2. Call the Open-Meteo weather API
  3. Extract the sunrise and sunset times
  ...

🔧 Extracting required MCP tools...
  Server: chuk-mcp-open-meteo
  Tool: get_forecast
  Parameters:
    - latitude (float): Location latitude
    - longitude (float): Location longitude
```

### 06_search_strategies.py - Search Provider Factory Pattern

**What it demonstrates:**
- Different search provider strategies (Keyword, Simple, Custom)
- Factory pattern for search providers
- Comparing search results across strategies
- Creating custom search providers
- Configuring search behavior (stop words, etc.)

**Search strategies shown:**
1. **KeywordSearch** - Word-based with stop word filtering (best for NL queries)
2. **SimpleSearch** - Direct substring matching (fast, exact)
3. **ExactMatchSearch** - Custom implementation example

**Key concepts:**
- SearchProvider interface
- SearchFactory pattern
- Pluggable search strategies
- Custom search implementation
- Search configuration

**Sample output:**
```
🔍 Strategy 1: Keyword Search
Query: 'How do I get sunset times?'
  1. Get Sunset and Sunrise Times

🔍 Strategy 2: Simple Search
Query: 'How do I get sunset times?'
  (no results)  # Can't match because full phrase not in title

🔍 Strategy 3: Custom Exact Match
Query: 'How do I get sunset times?'
  1. Get Sunset and Sunrise Times  # Matches "sunset" and "times"
```

**Use cases:**
- Switching search algorithms based on use case
- A/B testing different search strategies
- Domain-specific search customization
- Performance tuning
- Extracting steps and MCP tools
- Simulating playbook execution workflow

**Simulated workflow:**
1. User asks a question
2. Planner queries playbook repository
3. Playbook is returned as markdown
4. Planner parses steps and MCP tools
5. Planner creates execution plan
6. MCP tools are called with extracted parameters
7. Results are formatted and returned

**Key concepts:**
- Natural language → playbook mapping
- Markdown parsing
- Step extraction
- MCP tool identification
- Parameter extraction

**Sample output:**
```
🎯 User Question: 'What time is sunset in London today?'

📖 Parsing playbook...
✅ Found 6 sections

📝 Extracting steps...
  1. Determine the location coordinates
  2. Call the Open-Meteo weather API
  3. Extract the sunrise and sunset times
  ...

🔧 Extracting required MCP tools...
  Server: chuk-mcp-open-meteo
  Tool: get_forecast
  Parameters:
    - latitude (float): Location latitude
    - longitude (float): Location longitude
```

## Code Patterns

### Basic Setup Pattern

```python
from chuk_mcp_playbook.services.playbook_service import PlaybookService
from chuk_mcp_playbook.storage.factory import StorageFactory, StorageType

# Create storage
storage = StorageFactory.create(StorageType.MEMORY)

# Create service
service = PlaybookService(storage)

# Load playbooks
from pathlib import Path
playbooks_dir = Path(__file__).parent.parent / "playbooks"
await load_default_playbooks(service, playbooks_dir)
```

### Query Pattern

```python
# Natural language query
results = await service.query_playbooks("sunset times", top_k=3)

# Process results
for playbook in results:
    print(playbook.metadata.title)
    print(playbook.content)
```

### Creation Pattern

```python
# Create playbook
playbook = await service.create_playbook(
    title="My Playbook",
    content="# Playbook: ...",
    description="Description here",
    tags=["tag1", "tag2"],
    author="Your Name"
)
```

### Async Pattern

```python
# Concurrent operations
tasks = [
    service.query_playbooks("weather"),
    service.list_playbooks(),
    service.get_stats(),
]
results = await asyncio.gather(*tasks)
```

## Common Use Cases

### 1. Building a Playbook CLI Tool

```python
# Query playbooks from command line
import sys
question = sys.argv[1]
results = await service.query_playbooks(question, top_k=1)
if results:
    print(results[0].content)
```

### 2. REST API Wrapper

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/playbooks/search")
async def search(q: str):
    results = await service.query_playbooks(q)
    return [r.metadata.dict() for r in results]
```

### 3. AI Agent Integration

```python
# In your AI agent
user_query = "How do I check API health?"
playbooks = await service.query_playbooks(user_query, top_k=1)
if playbooks:
    # Parse playbook and execute steps
    execute_playbook(playbooks[0])
```

### 4. Dynamic Playbook Repository

```python
# Load playbooks from database
for record in database.get_playbooks():
    await service.create_playbook(
        title=record.title,
        content=record.content,
        ...
    )
```

## Testing Examples

Run all examples to verify your installation:

```bash
# From project root
for example in examples/*.py; do
    echo "Running $example..."
    python "$example"
    echo ""
done
```

Or use the provided test script:

```bash
chmod +x test_all_examples.sh
./test_all_examples.sh
```

## Next Steps

1. **Modify examples** - Change queries, add playbooks, experiment!
2. **Create custom storage** - Implement your own storage provider
3. **Build integrations** - Connect to your AI systems
4. **Extend functionality** - Add features to the playbook service

## Resources

- [Main README](../README.md) - Project overview
- [Architecture](../ARCHITECTURE.md) - Design documentation
- [Quick Start](../QUICKSTART.md) - Getting started guide
- [API Documentation](../src/chuk_mcp_playbook/) - Source code

## Support

If you have questions or find issues with the examples:
1. Check the main documentation
2. Review the source code
3. Open an issue on GitHub
4. Refer to the test suite in `../tests/`

Happy coding! 🚀
