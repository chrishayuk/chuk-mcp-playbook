# Quick Start Guide

## Installation

```bash
# Create virtual environment with uv
uv venv
source .venv/bin/activate

# Install the package
uv pip install -e .

# Install dev dependencies (optional)
uv pip install pytest pytest-asyncio
```

## Running the Server

The server supports two transport modes:

### STDIO Mode (Default - for Claude Desktop)

```bash
# Using uv (recommended)
uv run chuk-mcp-playbook

# Or with make
make run

# Or manually
source .venv/bin/activate
chuk-mcp-playbook
```

STDIO mode is designed for MCP clients like Claude Desktop and mcp-cli. It uses JSON-RPC over stdio for communication.

### HTTP Mode (for API/Web access)

```bash
# Using uv
uv run chuk-mcp-playbook http

# Or with make
make run-http
```

HTTP mode runs the server on `http://localhost:8000` and provides REST API access.

The server will:
1. Load all playbooks from `playbooks/` directory on startup
2. In HTTP mode: Log the number of playbooks loaded
3. In STDIO mode: Silently load and wait for JSON-RPC requests

## Using the Tools

### 1. Query for a Playbook

Ask a natural language question to get the most relevant playbook:

```python
# Tool: query_playbook
# Input:
{
  "question": "How do I get sunset times?",
  "top_k": 3
}

# Output: Full markdown playbook with steps
```

**Example Questions**:
- "How do I get sunset times?"
- "Show me how to get weather forecast"
- "What's the current weather?"

### 2. List All Playbooks

Get a list of all available playbooks:

```python
# Tool: list_playbooks
# Input: (none)

# Output:
[
  "Get Current Weather Conditions",
  "Get Sunset and Sunrise Times",
  "Get Weather Forecast"
]
```

### 3. Get a Specific Playbook

Retrieve a playbook by exact title:

```python
# Tool: get_playbook
# Input:
{
  "title": "Get Sunset and Sunrise Times"
}

# Output: Full markdown content
```

### 4. Add a New Playbook

Ingest a new playbook into the repository:

```python
# Tool: ingest_playbook
# Input:
{
  "title": "My Custom Playbook",
  "content": "# Playbook: My Custom Playbook\n\n## Description\n...",
  "description": "Does something useful",
  "tags": ["custom", "example"],
  "author": "Your Name"
}

# Output: "Successfully ingested playbook: My Custom Playbook"
```

### 5. Get Statistics

```python
# Tool: get_stats
# Input: (none)

# Output:
{
  "total_playbooks": 3
}
```

## Testing

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_loader.py -v

# Run with coverage
pytest tests/ --cov=chuk_mcp_playbook
```

## Adding New Playbooks

### Method 1: Add Markdown File

1. Create a new `.md` file in the `playbooks/` directory
2. Follow the playbook format (see example below)
3. Restart the server to load it

### Method 2: Use the API

Use the `ingest_playbook` tool to add playbooks programmatically.

## Playbook Format Template

```markdown
# Playbook: [Your Title Here]

## Description
Brief description of what this playbook accomplishes.

## Prerequisites
- Required inputs
- Required access or permissions

## Steps

1. First step in plain English
2. Second step with clear instructions
3. Third step...
4. Continue as needed

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
Expected result format
```

## Expected Response Format

Describe how the final output should look.

## Error Handling

- Error case 1: How to handle
- Error case 2: How to handle

## Notes

- Additional helpful information
- Tips and tricks
```

## Integration with AI Planner

To use with `chuk-ai-planner`:

1. Start the playbook server
2. Configure the planner to use this MCP server
3. Planner queries: `query_playbook("how to get weather?")`
4. Server returns: Markdown playbook with steps
5. Planner parses and executes the steps

**Workflow**:
```
User: "Get me sunset times for Tokyo"
    ↓
Planner: query_playbook("sunset times")
    ↓
Server: Returns sunset playbook
    ↓
Planner: Parses steps
    ↓
Planner: Calls chuk-mcp-open-meteo
    ↓
Result: "Sunrise: 6:30 AM, Sunset: 4:45 PM"
```

## Development

### Project Structure
```
chuk-mcp-playbook/
├── src/chuk_mcp_playbook/     # Source code
├── playbooks/                  # Markdown playbooks
├── tests/                      # Test suite
├── pyproject.toml             # Dependencies
└── README.md                  # Documentation
```

### Running with Development Changes

```bash
# After making changes, no reinstall needed (editable install)
python -m chuk_mcp_playbook.server
```

### Adding a Storage Provider

See `ARCHITECTURE.md` for details on extending with new storage backends.

## Troubleshooting

### Playbooks Not Loading

Check that:
1. `playbooks/` directory exists
2. Files are `.md` format
3. Files have proper markdown structure
4. Server has read permissions

View logs:
```bash
python -m chuk_mcp_playbook.server 2>&1 | grep -i playbook
```

### Import Errors

Ensure package is installed:
```bash
uv pip install -e .
```

### Tests Failing

Ensure test dependencies are installed:
```bash
uv pip install pytest pytest-asyncio
```

## Next Steps

1. **Add more playbooks**: Create markdown files in `playbooks/`
2. **Customize storage**: Implement a vector DB provider for semantic search
3. **Integrate with planner**: Connect to `chuk-ai-planner`
4. **Monitor usage**: Add logging and analytics

## Resources

- `README.md` - Project overview
- `ARCHITECTURE.md` - Detailed architecture documentation
- `playbooks/` - Example playbooks
- `tests/` - Test suite for reference
