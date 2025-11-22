"""Factory for creating storage providers."""

from enum import Enum

from chuk_mcp_playbook.search.base import SearchProvider
from chuk_mcp_playbook.storage.base import PlaybookStorage
from chuk_mcp_playbook.storage.providers.memory import InMemoryStorage


class StorageType(str, Enum):
    """Supported storage provider types."""

    MEMORY = "memory"
    # Future providers can be added here:
    # SQLITE = "sqlite"
    # POSTGRES = "postgres"
    # CHROMA = "chroma"


class StorageFactory:
    """Factory for creating playbook storage providers."""

    @staticmethod
    def create(
        storage_type: StorageType = StorageType.MEMORY,
        search_provider: SearchProvider | None = None,
        **kwargs
    ) -> PlaybookStorage:
        """
        Create a storage provider instance.

        Args:
            storage_type: Type of storage provider to create
            search_provider: Optional search provider for querying
            **kwargs: Provider-specific configuration

        Returns:
            PlaybookStorage instance

        Raises:
            ValueError: If storage_type is not supported

        Examples:
            >>> # Default storage with keyword search
            >>> storage = StorageFactory.create()
            >>>
            >>> # Storage with custom search provider
            >>> from chuk_mcp_playbook.search.factory import SearchFactory, SearchType
            >>> search = SearchFactory.create(SearchType.SIMPLE)
            >>> storage = StorageFactory.create(search_provider=search)
        """
        if storage_type == StorageType.MEMORY:
            return InMemoryStorage(search_provider=search_provider, **kwargs)
        # Future providers:
        # elif storage_type == StorageType.SQLITE:
        #     return SQLiteStorage(search_provider=search_provider, **kwargs)
        # elif storage_type == StorageType.CHROMA:
        #     return ChromaStorage(**kwargs)  # Would use built-in vector search
        else:
            raise ValueError(f"Unsupported storage type: {storage_type}")
