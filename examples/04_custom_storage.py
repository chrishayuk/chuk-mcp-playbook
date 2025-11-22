#!/usr/bin/env python3
"""
Custom Storage Provider Example
================================

This example demonstrates how to:
1. Create a custom storage provider
2. Implement the PlaybookStorage interface
3. Use the factory pattern to instantiate it
4. Extend the system with custom functionality
"""

import asyncio
from pathlib import Path
from typing import Optional

from chuk_mcp_playbook.models.playbook import Playbook
from chuk_mcp_playbook.services.playbook_service import PlaybookService
from chuk_mcp_playbook.storage.base import PlaybookStorage
from chuk_mcp_playbook.loader import load_default_playbooks


class LoggingStorage(PlaybookStorage):
    """
    Custom storage provider that wraps another storage and logs all operations.

    This demonstrates how to:
    - Implement the PlaybookStorage interface
    - Wrap an existing storage provider
    - Add custom behavior (logging in this case)
    """

    def __init__(self, wrapped_storage: PlaybookStorage):
        self.storage = wrapped_storage
        self.operation_count = 0

    def _log(self, operation: str, details: str = ""):
        """Log an operation."""
        self.operation_count += 1
        print(f"  📝 [{self.operation_count}] {operation}: {details}")

    async def add_playbook(self, playbook: Playbook) -> None:
        """Add a playbook with logging."""
        self._log("ADD", f"'{playbook.metadata.title}'")
        await self.storage.add_playbook(playbook)

    async def get_playbook(self, title: str) -> Optional[Playbook]:
        """Get a playbook with logging."""
        self._log("GET", f"'{title}'")
        result = await self.storage.get_playbook(title)
        if result:
            self._log("GET_RESULT", "Found")
        else:
            self._log("GET_RESULT", "Not found")
        return result

    async def query(
        self, question: str, top_k: int = 3, tags: Optional[list[str]] = None
    ) -> list[Playbook]:
        """Query playbooks with logging."""
        self._log("QUERY", f"'{question}' (top_k={top_k})")
        results = await self.storage.query(question, top_k, tags)
        self._log("QUERY_RESULT", f"Found {len(results)} playbooks")
        return results

    async def list_all(self) -> list[str]:
        """List all playbooks with logging."""
        self._log("LIST_ALL", "")
        results = await self.storage.list_all()
        self._log("LIST_RESULT", f"{len(results)} playbooks")
        return results

    async def delete_playbook(self, title: str) -> bool:
        """Delete a playbook with logging."""
        self._log("DELETE", f"'{title}'")
        result = await self.storage.delete_playbook(title)
        self._log("DELETE_RESULT", "Deleted" if result else "Not found")
        return result

    async def clear(self) -> None:
        """Clear all playbooks with logging."""
        self._log("CLEAR", "All playbooks")
        await self.storage.clear()

    async def count(self) -> int:
        """Count playbooks with logging."""
        self._log("COUNT", "")
        result = await self.storage.count()
        self._log("COUNT_RESULT", f"{result} playbooks")
        return result


class CachedStorage(PlaybookStorage):
    """
    Custom storage provider with simple caching.

    Demonstrates:
    - Caching frequently accessed playbooks
    - Cache invalidation
    - Performance optimization
    """

    def __init__(self, wrapped_storage: PlaybookStorage):
        self.storage = wrapped_storage
        self._cache: dict[str, Playbook] = {}
        self.cache_hits = 0
        self.cache_misses = 0

    async def add_playbook(self, playbook: Playbook) -> None:
        """Add playbook and update cache."""
        await self.storage.add_playbook(playbook)
        self._cache[playbook.metadata.title] = playbook

    async def get_playbook(self, title: str) -> Optional[Playbook]:
        """Get playbook with caching."""
        if title in self._cache:
            self.cache_hits += 1
            print(f"  💨 Cache HIT for '{title}' (hits: {self.cache_hits})")
            return self._cache[title]

        self.cache_misses += 1
        print(f"  🔍 Cache MISS for '{title}' (misses: {self.cache_misses})")
        result = await self.storage.get_playbook(title)
        if result:
            self._cache[title] = result
        return result

    async def query(
        self, question: str, top_k: int = 3, tags: Optional[list[str]] = None
    ) -> list[Playbook]:
        """Query (no caching for queries)."""
        return await self.storage.query(question, top_k, tags)

    async def list_all(self) -> list[str]:
        """List all."""
        return await self.storage.list_all()

    async def delete_playbook(self, title: str) -> bool:
        """Delete and invalidate cache."""
        if title in self._cache:
            del self._cache[title]
        return await self.storage.delete_playbook(title)

    async def clear(self) -> None:
        """Clear and invalidate cache."""
        self._cache.clear()
        await self.storage.clear()

    async def count(self) -> int:
        """Count."""
        return await self.storage.count()


async def main():
    """Run custom storage example."""
    print("=" * 70)
    print("Example 4: Custom Storage Providers")
    print("=" * 70)
    print()

    # Example 1: Logging Storage
    print("📝 Example 1: Logging Storage Provider")
    print("-" * 70)
    from chuk_mcp_playbook.storage.factory import StorageFactory, StorageType

    base_storage = StorageFactory.create(StorageType.MEMORY)
    logging_storage = LoggingStorage(base_storage)
    service = PlaybookService(logging_storage)

    print("Loading playbooks...")
    playbooks_dir = Path(__file__).parent.parent / "playbooks"
    await load_default_playbooks(service, playbooks_dir)
    print()

    print("Performing operations (watch the logs)...")
    await service.query_playbooks("sunset", top_k=1)
    await service.get_playbook("Get Sunset and Sunrise Times")
    await service.list_playbooks()
    stats = await service.get_stats()
    print()
    print(f"Total operations logged: {logging_storage.operation_count}")
    print()

    # Example 2: Cached Storage
    print("💨 Example 2: Cached Storage Provider")
    print("-" * 70)
    base_storage2 = StorageFactory.create(StorageType.MEMORY)
    cached_storage = CachedStorage(base_storage2)
    service2 = PlaybookService(cached_storage)

    print("Loading playbooks...")
    await load_default_playbooks(service2, playbooks_dir)
    print()

    print("First access (will miss cache):")
    await service2.get_playbook("Get Sunset and Sunrise Times")
    print()

    print("Second access (will hit cache):")
    await service2.get_playbook("Get Sunset and Sunrise Times")
    print()

    print("Third access (will hit cache):")
    await service2.get_playbook("Get Sunset and Sunrise Times")
    print()

    print(f"Cache Statistics:")
    print(f"  Hits: {cached_storage.cache_hits}")
    print(f"  Misses: {cached_storage.cache_misses}")
    print(f"  Hit Rate: {cached_storage.cache_hits / (cached_storage.cache_hits + cached_storage.cache_misses) * 100:.1f}%")
    print()

    # Example 3: Combining both!
    print("🔀 Example 3: Combining Logging + Caching")
    print("-" * 70)
    base_storage3 = StorageFactory.create(StorageType.MEMORY)
    cached_and_logged = LoggingStorage(CachedStorage(base_storage3))
    service3 = PlaybookService(cached_and_logged)

    print("Loading playbooks...")
    await load_default_playbooks(service3, playbooks_dir)
    print()

    print("Accessing same playbook 3 times:")
    for i in range(3):
        print(f"\nAccess {i + 1}:")
        await service3.get_playbook("Get Weather Forecast")
    print()

    print("✅ Example complete!")
    print()
    print("💡 Key Takeaways:")
    print("  - Custom storage providers implement PlaybookStorage interface")
    print("  - Can wrap existing providers to add functionality")
    print("  - Logging provider: Tracks all operations")
    print("  - Caching provider: Improves read performance")
    print("  - Providers can be composed/layered")


if __name__ == "__main__":
    asyncio.run(main())
