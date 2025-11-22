#!/usr/bin/env python3
"""
Search Strategies Example
==========================

This example demonstrates:
1. Different search provider strategies
2. Factory pattern for search providers
3. Comparing search results across strategies
4. Custom search provider implementation
"""

import asyncio
from pathlib import Path

from chuk_mcp_playbook.services.playbook_service import PlaybookService
from chuk_mcp_playbook.storage.factory import StorageFactory, StorageType
from chuk_mcp_playbook.search.factory import SearchFactory, SearchType
from chuk_mcp_playbook.search.base import SearchProvider
from chuk_mcp_playbook.models.playbook import Playbook
from chuk_mcp_playbook.loader import load_default_playbooks


class ExactMatchSearch(SearchProvider):
    """
    Custom search provider: Exact word matching only.

    Demonstrates how to create a custom search strategy.
    """

    def score(self, playbook: Playbook, query: str) -> tuple[bool, float]:
        """Score based on exact word matches."""
        query_words = set(query.lower().split())
        title_words = set(playbook.metadata.title.lower().split())

        # Count exact matches
        matches = query_words & title_words

        if matches:
            # Score based on proportion of query words matched
            score = len(matches) / len(query_words)
            return (True, score)

        return (False, 0.0)


async def compare_search_strategies(service, query: str):
    """Compare results from different search strategies."""
    print(f"Query: '{query}'")
    print("-" * 70)

    results = await service.query_playbooks(query, top_k=3)
    for i, playbook in enumerate(results, 1):
        print(f"  {i}. {playbook.metadata.title}")

    if not results:
        print("  (no results)")


async def main():
    """Run search strategies example."""
    print("=" * 70)
    print("Example 6: Search Strategies & Factory Pattern")
    print("=" * 70)
    print()

    playbooks_dir = Path(__file__).parent.parent / "playbooks"

    # Test queries
    test_queries = [
        "How do I get sunset times?",
        "forecast",
        "current weather",
    ]

    # Strategy 1: Keyword Search (default - filters stop words)
    print("🔍 Strategy 1: Keyword Search (Default)")
    print("   Features: Stop word filtering, word-based matching")
    print("=" * 70)

    keyword_search = SearchFactory.create(SearchType.KEYWORD)
    storage1 = StorageFactory.create(StorageType.MEMORY, search_provider=keyword_search)
    service1 = PlaybookService(storage1)
    await load_default_playbooks(service1, playbooks_dir)

    for query in test_queries:
        await compare_search_strategies(service1, query)
        print()

    print()

    # Strategy 2: Simple Search (substring matching)
    print("🔍 Strategy 2: Simple Search")
    print("   Features: Direct substring matching, no filtering")
    print("=" * 70)

    simple_search = SearchFactory.create(SearchType.SIMPLE)
    storage2 = StorageFactory.create(StorageType.MEMORY, search_provider=simple_search)
    service2 = PlaybookService(storage2)
    await load_default_playbooks(service2, playbooks_dir)

    for query in test_queries:
        await compare_search_strategies(service2, query)
        print()

    print()

    # Strategy 3: Custom Exact Match Search
    print("🔍 Strategy 3: Custom Exact Match Search")
    print("   Features: Custom implementation, exact word matches only")
    print("=" * 70)

    exact_search = ExactMatchSearch()
    storage3 = StorageFactory.create(StorageType.MEMORY, search_provider=exact_search)
    service3 = PlaybookService(storage3)
    await load_default_playbooks(service3, playbooks_dir)

    for query in test_queries:
        await compare_search_strategies(service3, query)
        print()

    print()

    # Detailed comparison for one query
    print("📊 Detailed Comparison")
    print("=" * 70)

    comparison_query = "weather forecast information"
    print(f"Query: '{comparison_query}'")
    print()

    strategies = [
        ("Keyword", service1),
        ("Simple", service2),
        ("Exact Match", service3),
    ]

    for name, service in strategies:
        print(f"{name} Search:")
        results = await service.query_playbooks(comparison_query, top_k=2)
        if results:
            for i, playbook in enumerate(results, 1):
                print(f"  {i}. {playbook.metadata.title}")
        else:
            print("  (no results)")
        print()

    # Performance note
    print("💡 Key Differences:")
    print("  - Keyword: Best for natural language queries (filters 'how', 'do', 'i')")
    print("  - Simple: Fast substring matching (good for short, specific queries)")
    print("  - Exact Match: Requires exact word matches (very precise)")
    print()

    # Custom stop words example
    print("🎛️  Customizing Keyword Search")
    print("=" * 70)

    # Create keyword search with custom stop words
    custom_stops = {'how', 'what', 'when'}  # Minimal stop words
    custom_keyword = KeywordSearch(stop_words=custom_stops)
    storage4 = StorageFactory.create(StorageType.MEMORY, search_provider=custom_keyword)
    service4 = PlaybookService(storage4)
    await load_default_playbooks(service4, playbooks_dir)

    query = "How do I get weather information?"
    print(f"Query: '{query}'")
    print()
    print("Default stop words (many filtered):")
    results_default = await service1.query_playbooks(query, top_k=2)
    for playbook in results_default:
        print(f"  - {playbook.metadata.title}")
    print()

    print("Custom stop words (only 'how', 'what', 'when' filtered):")
    results_custom = await service4.query_playbooks(query, top_k=2)
    for playbook in results_custom:
        print(f"  - {playbook.metadata.title}")
    print()

    print("✅ Example complete!")
    print()
    print("📚 Next Steps:")
    print("  - Implement your own SearchProvider for domain-specific matching")
    print("  - Add fuzzy matching for typo tolerance")
    print("  - Integrate semantic/vector search for better understanding")
    print("  - Combine multiple strategies (hybrid search)")


# Import for custom stop words
from chuk_mcp_playbook.search.providers.keyword import KeywordSearch


if __name__ == "__main__":
    asyncio.run(main())
