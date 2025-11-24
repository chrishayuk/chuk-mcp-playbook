"""Test playbook loader functionality."""

import pytest
from pathlib import Path

from chuk_mcp_playbook.loader import PlaybookLoader, load_default_playbooks
from chuk_mcp_playbook.services.playbook_service import PlaybookService
from chuk_mcp_playbook.storage.factory import StorageFactory, StorageType


@pytest.mark.asyncio
async def test_load_from_directory():
    """Test loading playbooks from directory (recursively includes subdirectories)."""
    storage = StorageFactory.create(StorageType.MEMORY)
    service = PlaybookService(storage)

    # Get the playbooks directory
    test_file = Path(__file__)
    project_root = test_file.parent.parent
    playbooks_dir = project_root / "playbooks"

    # Load playbooks (now includes all subdirectories)
    count = await load_default_playbooks(service, playbooks_dir)

    # Should have loaded multiple playbooks (including subdirectories like Weather/)
    # We have weather playbooks + mermaid diagram playbooks + scenario playbooks
    assert count >= 50, f"Expected at least 50 playbooks, got {count}"

    # Verify they're in storage
    stats = await service.get_stats()
    assert stats["total_playbooks"] >= 50

    # Verify we can query them
    results = await service.query_playbooks("sunset")
    assert len(results) > 0

    # Verify titles
    titles = await service.list_playbooks()
    assert len(titles) >= 50


@pytest.mark.asyncio
async def test_query_sunset_playbook():
    """Test querying for sunset playbook."""
    storage = StorageFactory.create(StorageType.MEMORY)
    service = PlaybookService(storage)

    # Load playbooks
    test_file = Path(__file__)
    playbooks_dir = test_file.parent.parent / "playbooks"
    await load_default_playbooks(service, playbooks_dir)

    # Query for sunset
    results = await service.query_playbooks("sunset", top_k=1)
    assert len(results) == 1

    playbook = results[0]
    assert "sunset" in playbook.metadata.title.lower() or "sunrise" in playbook.metadata.title.lower()
    assert "## Steps" in playbook.content
    assert "## MCP Tools Required" in playbook.content


@pytest.mark.asyncio
async def test_query_weather_forecast():
    """Test querying for weather forecast playbook."""
    storage = StorageFactory.create(StorageType.MEMORY)
    service = PlaybookService(storage)

    # Load playbooks
    test_file = Path(__file__)
    playbooks_dir = test_file.parent.parent / "playbooks"
    await load_default_playbooks(service, playbooks_dir)

    # Query for forecast
    results = await service.query_playbooks("forecast", top_k=1)
    assert len(results) == 1

    playbook = results[0]
    assert "forecast" in playbook.metadata.title.lower()
    assert "chuk-mcp-open-meteo" in playbook.content
