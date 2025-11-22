"""Factory for creating search providers."""

from enum import Enum

from chuk_mcp_playbook.search.base import SearchProvider
from chuk_mcp_playbook.search.providers.keyword import KeywordSearch
from chuk_mcp_playbook.search.providers.simple import SimpleSearch


class SearchType(str, Enum):
    """Supported search provider types."""

    KEYWORD = "keyword"  # Keyword-based with stop word filtering (default, best for NL queries)
    SIMPLE = "simple"    # Simple substring matching (fast, exact)
    # Future providers:
    # FUZZY = "fuzzy"      # Fuzzy string matching
    # SEMANTIC = "semantic"  # Vector/embedding-based search
    # HYBRID = "hybrid"    # Combination of multiple strategies


class SearchFactory:
    """Factory for creating search provider instances."""

    @staticmethod
    def create(search_type: SearchType = SearchType.KEYWORD, **kwargs) -> SearchProvider:
        """
        Create a search provider instance.

        Args:
            search_type: Type of search provider to create
            **kwargs: Provider-specific configuration

        Returns:
            SearchProvider instance

        Raises:
            ValueError: If search_type is not supported

        Examples:
            >>> # Default keyword search
            >>> search = SearchFactory.create()
            >>>
            >>> # Simple substring search
            >>> search = SearchFactory.create(SearchType.SIMPLE)
            >>>
            >>> # Keyword search with custom stop words
            >>> custom_stops = {'the', 'a', 'an'}
            >>> search = SearchFactory.create(SearchType.KEYWORD, stop_words=custom_stops)
        """
        if search_type == SearchType.KEYWORD:
            return KeywordSearch(**kwargs)
        elif search_type == SearchType.SIMPLE:
            return SimpleSearch(**kwargs)
        # Future providers:
        # elif search_type == SearchType.FUZZY:
        #     return FuzzySearch(**kwargs)
        # elif search_type == SearchType.SEMANTIC:
        #     return SemanticSearch(**kwargs)
        else:
            raise ValueError(f"Unsupported search type: {search_type}")
