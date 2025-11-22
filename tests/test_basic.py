"""Basic tests for playbook server."""

import pytest

from chuk_mcp_playbook.models.playbook import Playbook, PlaybookMetadata
from chuk_mcp_playbook.services.playbook_service import PlaybookService
from chuk_mcp_playbook.storage.factory import StorageFactory, StorageType


@pytest.mark.asyncio
async def test_create_and_query_playbook():
    """Test creating and querying a playbook."""
    # Create service with in-memory storage
    storage = StorageFactory.create(StorageType.MEMORY)
    service = PlaybookService(storage)

    # Create a playbook
    playbook = await service.create_playbook(
        title="Test Playbook",
        content="# Test Playbook\n\nThis is a test.",
        description="A test playbook for sunset queries",
        tags=["test", "sunset"],
    )

    assert playbook.metadata.title == "Test Playbook"
    assert len(playbook.metadata.tags) == 2

    # Query for it
    results = await service.query_playbooks("sunset")
    assert len(results) == 1
    assert results[0].metadata.title == "Test Playbook"


@pytest.mark.asyncio
async def test_playbook_matching():
    """Test playbook query matching logic."""
    metadata = PlaybookMetadata(
        title="Get Sunset Times",
        description="Retrieve sunset and sunrise times",
        tags=["weather", "sunset"],
    )
    playbook = Playbook(metadata=metadata, content="Test content")

    # Should match on title
    matches, score = playbook.matches_query("sunset")
    assert matches
    assert score > 0

    # Should match on tags
    matches, score = playbook.matches_query("weather")
    assert matches
    assert score > 0

    # Should not match unrelated query
    matches, score = playbook.matches_query("database")
    assert not matches
    assert score == 0


@pytest.mark.asyncio
async def test_storage_operations():
    """Test basic storage operations."""
    storage = StorageFactory.create(StorageType.MEMORY)

    metadata = PlaybookMetadata(
        title="Test",
        description="Test playbook",
        tags=["test"],
    )
    playbook = Playbook(metadata=metadata, content="Content")

    # Add playbook
    await storage.add_playbook(playbook)

    # Count
    count = await storage.count()
    assert count == 1

    # Get by title
    retrieved = await storage.get_playbook("Test")
    assert retrieved is not None
    assert retrieved.metadata.title == "Test"

    # List all
    titles = await storage.list_all()
    assert "Test" in titles

    # Delete
    deleted = await storage.delete_playbook("Test")
    assert deleted
    count = await storage.count()
    assert count == 0
