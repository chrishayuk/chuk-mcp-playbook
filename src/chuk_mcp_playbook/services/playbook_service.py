"""Service layer for playbook operations."""

from typing import Optional

from chuk_mcp_playbook.models.playbook import Playbook, PlaybookMetadata
from chuk_mcp_playbook.storage.base import PlaybookStorage


class PlaybookService:
    """Service for managing playbook operations."""

    def __init__(self, storage: PlaybookStorage):
        self.storage = storage

    async def create_playbook(
        self,
        title: str,
        content: str,
        description: str,
        tags: Optional[list[str]] = None,
        author: Optional[str] = None,
    ) -> Playbook:
        """Create and store a new playbook."""
        metadata = PlaybookMetadata(
            title=title,
            description=description,
            tags=tags or [],
            author=author,
        )
        playbook = Playbook(metadata=metadata, content=content)
        await self.storage.add_playbook(playbook)
        return playbook

    async def get_playbook(self, title: str) -> Optional[Playbook]:
        """Retrieve a playbook by title."""
        return await self.storage.get_playbook(title)

    async def query_playbooks(
        self,
        question: str,
        top_k: int = 3,
        tags: Optional[list[str]] = None,
    ) -> list[Playbook]:
        """Query playbooks with a natural language question."""
        return await self.storage.query(question, top_k=top_k, tags=tags)

    async def list_playbooks(self) -> list[str]:
        """List all playbook titles."""
        return await self.storage.list_all()

    async def delete_playbook(self, title: str) -> bool:
        """Delete a playbook."""
        return await self.storage.delete_playbook(title)

    async def get_stats(self) -> dict[str, int]:
        """Get storage statistics."""
        count = await self.storage.count()
        return {"total_playbooks": count}
