"""In-memory storage provider with pluggable search."""

from typing import Optional

from chuk_mcp_playbook.models.playbook import Playbook
from chuk_mcp_playbook.search.base import SearchProvider
from chuk_mcp_playbook.search.factory import SearchFactory, SearchType
from chuk_mcp_playbook.storage.base import PlaybookStorage


class InMemoryStorage(PlaybookStorage):
    """
    In-memory storage provider using dictionaries for fast lookups.

    Supports pluggable search strategies via SearchProvider.
    """

    def __init__(self, search_provider: SearchProvider | None = None):
        """
        Initialize storage.

        Args:
            search_provider: Optional search provider. Defaults to KeywordSearch.
        """
        self._playbooks: dict[str, Playbook] = {}
        self._search = search_provider or SearchFactory.create(SearchType.KEYWORD)

    async def add_playbook(self, playbook: Playbook) -> None:
        """Add or update a playbook in storage."""
        self._playbooks[playbook.metadata.title] = playbook

    async def get_playbook(self, title: str) -> Optional[Playbook]:
        """Get a playbook by exact title."""
        return self._playbooks.get(title)

    async def query(self, question: str, top_k: int = 3, tags: Optional[list[str]] = None) -> list[Playbook]:
        """
        Query playbooks using the configured search provider.
        Returns top_k most relevant playbooks sorted by relevance.
        """
        # Filter by tags if provided
        playbooks = list(self._playbooks.values())
        if tags:
            playbooks = [
                p for p in playbooks
                if any(tag in p.metadata.tags for tag in tags)
            ]

        # Use search provider to find and rank results
        return self._search.search(playbooks, question, top_k=top_k)

    async def list_all(self) -> list[str]:
        """List all playbook titles sorted alphabetically."""
        return sorted(self._playbooks.keys())

    async def delete_playbook(self, title: str) -> bool:
        """Delete a playbook by title. Returns True if deleted, False if not found."""
        if title in self._playbooks:
            del self._playbooks[title]
            return True
        return False

    async def clear(self) -> None:
        """Clear all playbooks."""
        self._playbooks.clear()

    async def count(self) -> int:
        """Return number of playbooks in storage."""
        return len(self._playbooks)
