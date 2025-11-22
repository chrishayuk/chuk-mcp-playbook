"""Abstract base class for playbook storage providers."""

from abc import ABC, abstractmethod
from typing import Optional

from chuk_mcp_playbook.models.playbook import Playbook


class PlaybookStorage(ABC):
    """Abstract base class for playbook storage providers."""

    @abstractmethod
    async def add_playbook(self, playbook: Playbook) -> None:
        """Add or update a playbook in storage."""
        pass

    @abstractmethod
    async def get_playbook(self, title: str) -> Optional[Playbook]:
        """Get a playbook by exact title."""
        pass

    @abstractmethod
    async def query(self, question: str, top_k: int = 3, tags: Optional[list[str]] = None) -> list[Playbook]:
        """
        Query playbooks using the provider's search mechanism.
        Returns top_k most relevant playbooks sorted by relevance.
        """
        pass

    @abstractmethod
    async def list_all(self) -> list[str]:
        """List all playbook titles."""
        pass

    @abstractmethod
    async def delete_playbook(self, title: str) -> bool:
        """Delete a playbook by title. Returns True if deleted, False if not found."""
        pass

    @abstractmethod
    async def clear(self) -> None:
        """Clear all playbooks (useful for testing)."""
        pass

    @abstractmethod
    async def count(self) -> int:
        """Return number of playbooks in storage."""
        pass
