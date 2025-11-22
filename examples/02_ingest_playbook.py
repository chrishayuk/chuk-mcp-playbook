#!/usr/bin/env python3
"""
Playbook Ingestion Example
===========================

This example demonstrates how to:
1. Create new playbooks programmatically
2. Ingest them into the storage
3. Query for the newly added playbooks
"""

import asyncio
from pathlib import Path

from chuk_mcp_playbook.services.playbook_service import PlaybookService
from chuk_mcp_playbook.storage.factory import StorageFactory, StorageType
from chuk_mcp_playbook.loader import load_default_playbooks


async def main():
    """Run playbook ingestion example."""
    print("=" * 70)
    print("Example 2: Ingesting New Playbooks")
    print("=" * 70)
    print()

    # Create storage and service
    storage = StorageFactory.create(StorageType.MEMORY)
    service = PlaybookService(storage)

    # Load existing playbooks
    playbooks_dir = Path(__file__).parent.parent / "playbooks"
    count = await load_default_playbooks(service, playbooks_dir)
    print(f"📚 Loaded {count} existing playbooks")
    print()

    # Create a new playbook programmatically
    new_playbook_content = """# Playbook: Check API Health

## Description
This playbook demonstrates how to check the health status of an API endpoint
and verify it's responding correctly.

## Prerequisites
- API endpoint URL
- Expected response status code
- Optional: Authentication credentials

## Steps

1. Prepare the HTTP request with appropriate headers
2. Send a GET request to the health check endpoint
3. Verify the response status code matches expectations
4. Check the response body for health indicators
5. Log the results and alert if unhealthy

## MCP Tools Required

### http-client
- **Tool**: `http_get`
- **Parameters**:
  - `url` (string): The API health endpoint URL
  - `headers` (dict): Optional headers including authentication
  - `timeout` (int): Request timeout in seconds (default: 5)

## Example Usage

**Input**: "Check if the API at https://api.example.com/health is up"

**Process**:
1. Extract URL: https://api.example.com/health
2. Call http_get with URL and timeout
3. Check status code == 200
4. Verify response body contains "status": "healthy"

**Output**:
```
API Health Status: ✅ Healthy
Response Time: 145ms
Status: All systems operational
```

## Expected Response Format

```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00Z",
  "services": {
    "database": "up",
    "cache": "up",
    "queue": "up"
  }
}
```

## Error Handling

- Connection timeout: Retry up to 3 times with exponential backoff
- 5xx status codes: Report service degradation
- 4xx status codes: Check authentication or endpoint URL
- Invalid JSON response: Log raw response and investigate

## Notes

- Health checks should be fast (< 1 second response time)
- Monitor trends over time to detect degradation
- Set up alerts for consecutive failures
- Consider using circuit breaker pattern for dependent services
"""

    print("➕ Creating new playbook...")
    playbook = await service.create_playbook(
        title="Check API Health",
        content=new_playbook_content,
        description="Demonstrates how to check API health status and verify responses",
        tags=["api", "health", "monitoring", "http"],
        author="Example Script",
    )
    print(f"✅ Created: {playbook.metadata.title}")
    print(f"   Tags: {', '.join(playbook.metadata.tags)}")
    print(f"   Author: {playbook.metadata.author}")
    print()

    # Create another playbook
    print("➕ Creating another playbook...")
    database_playbook = """# Playbook: Query Database Records

## Description
Query records from a database table with filtering and sorting.

## Steps

1. Connect to the database using credentials
2. Construct SQL query with WHERE clause for filtering
3. Add ORDER BY clause for sorting
4. Execute query with parameter binding
5. Fetch and format results

## MCP Tools Required

### database-client
- **Tool**: `execute_query`
- **Parameters**:
  - `connection_string` (string): Database connection
  - `query` (string): SQL query to execute
  - `parameters` (dict): Query parameters
"""

    await service.create_playbook(
        title="Query Database Records",
        content=database_playbook,
        description="Query and filter database records with SQL",
        tags=["database", "sql", "query"],
        author="Example Script",
    )
    print("✅ Created: Query Database Records")
    print()

    # List all playbooks (including new ones)
    print("📋 All playbooks in repository:")
    titles = await service.list_playbooks()
    for i, title in enumerate(titles, 1):
        print(f"  {i}. {title}")
    print()

    # Query for the new playbooks
    print("🔍 Searching for 'API health'...")
    results = await service.query_playbooks("API health", top_k=2)
    for result in results:
        print(f"  ✅ {result.metadata.title}")
        print(f"     Tags: {', '.join(result.metadata.tags)}")
    print()

    print("🔍 Searching for 'database query'...")
    results = await service.query_playbooks("database query", top_k=2)
    for result in results:
        print(f"  ✅ {result.metadata.title}")
        print(f"     Tags: {', '.join(result.metadata.tags)}")
    print()

    # Get updated statistics
    stats = await service.get_stats()
    print(f"📊 Final Statistics: {stats}")
    print()

    print("✅ Example complete!")


if __name__ == "__main__":
    asyncio.run(main())
