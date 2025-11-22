"""Main MCP server implementation."""

import logging
import sys
from typing import Any

from chuk_mcp_server import run, tool

from chuk_mcp_playbook.loader import load_default_playbooks
from chuk_mcp_playbook.services.playbook_service import PlaybookService
from chuk_mcp_playbook.storage.factory import StorageFactory, StorageType

# Configure logging
# In STDIO mode, we need to be quiet to avoid polluting the JSON-RPC stream
# Only log to stderr, and only warnings/errors
logging.basicConfig(
    level=logging.WARNING,
    format="%(levelname)s:%(name)s:%(message)s",
    stream=sys.stderr,
)

logger = logging.getLogger(__name__)

# Initialize storage and service (global for all tools)
storage = StorageFactory.create(StorageType.MEMORY)
playbook_service = PlaybookService(storage)


# ============================================================================
# MCP Tools - Type-safe and async native
# ============================================================================


@tool
async def query_playbook(question: str, top_k: int = 3) -> str:
    """
    Query the playbook repository with a natural language question.

    Args:
        question: Natural language question (e.g., "How do I get sunset times?")
        top_k: Maximum number of playbooks to return (default: 3)

    Returns:
        Markdown-formatted playbook(s) that answer the question
    """
    logger.info(f"Querying playbooks: {question}")

    playbooks = await playbook_service.query_playbooks(question=question, top_k=top_k)

    if not playbooks:
        return f"No playbooks found matching: {question}"

    # Return the top result's content (most relevant)
    top_playbook = playbooks[0]
    return top_playbook.content


@tool
async def ingest_playbook(
    title: str,
    content: str,
    description: str,
    tags: list[str] | None = None,
    author: str | None = None,
) -> str:
    """
    Ingest a new playbook into the repository.

    Args:
        title: Title of the playbook
        content: Markdown content of the playbook
        description: Brief description of what this playbook does
        tags: Optional list of tags for categorization
        author: Optional author name

    Returns:
        Success message with playbook details
    """
    logger.info(f"Ingesting playbook: {title}")

    playbook = await playbook_service.create_playbook(
        title=title,
        content=content,
        description=description,
        tags=tags,
        author=author,
    )

    return f"Successfully ingested playbook: {playbook.metadata.title}"


@tool
async def list_playbooks() -> list[str]:
    """
    List all available playbooks in the repository.

    Returns:
        List of playbook titles
    """
    logger.info("Listing all playbooks")
    return await playbook_service.list_playbooks()


@tool
async def get_playbook(title: str) -> str:
    """
    Retrieve a specific playbook by exact title.

    Args:
        title: Exact title of the playbook

    Returns:
        Markdown content of the playbook or error message
    """
    logger.info(f"Getting playbook: {title}")

    playbook = await playbook_service.get_playbook(title)

    if not playbook:
        return f"Playbook not found: {title}"

    return playbook.content


@tool
async def get_stats() -> dict[str, Any]:
    """
    Get repository statistics.

    Returns:
        Dictionary with stats (total playbooks, etc.)
    """
    logger.info("Getting repository stats")
    return await playbook_service.get_stats()


# ============================================================================
# Server Entry Point
# ============================================================================


def main():
    """Run the MCP Playbook server."""
    # Check if transport is specified in command line args
    # Default to stdio for MCP compatibility (Claude Desktop, mcp-cli)
    transport = "stdio"

    # Allow HTTP mode via command line
    if len(sys.argv) > 1:
        if sys.argv[1] in ["http", "--http"]:
            transport = "http"
            # Only log in HTTP mode
            logger.warning("Starting Chuk MCP Playbook Server in HTTP mode")
        elif sys.argv[1] in ["--transport"]:
            if len(sys.argv) > 2:
                transport = sys.argv[2]

    # Suppress chuk_mcp_server logging in STDIO mode
    if transport == "stdio":
        # Set chuk_mcp_server loggers to ERROR only
        logging.getLogger("chuk_mcp_server").setLevel(logging.ERROR)
        logging.getLogger("chuk_mcp_server.core").setLevel(logging.ERROR)
        logging.getLogger("chuk_mcp_server.stdio_transport").setLevel(logging.ERROR)

    # Load default playbooks before starting server
    try:
        import asyncio
        count = asyncio.run(load_default_playbooks(playbook_service))
        if transport == "http":
            logger.warning(f"Successfully loaded {count} playbooks")
    except Exception as e:
        if transport == "http":
            logger.error(f"Error loading playbooks: {e}")

    run(transport=transport)


if __name__ == "__main__":
    main()
