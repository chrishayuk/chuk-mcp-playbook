#!/usr/bin/env python3
"""
Basic Query Example
===================

This example demonstrates how to:
1. Create a playbook service with in-memory storage
2. Load playbooks from the playbooks directory
3. Query for playbooks using natural language
4. Display the results
"""

import asyncio
from pathlib import Path

from chuk_mcp_playbook.services.playbook_service import PlaybookService
from chuk_mcp_playbook.storage.factory import StorageFactory, StorageType
from chuk_mcp_playbook.loader import load_default_playbooks


async def main():
    """Run basic query example."""
    print("=" * 70)
    print("Example 1: Basic Playbook Query")
    print("=" * 70)
    print()

    # 1. Create storage and service
    print("📦 Creating in-memory storage...")
    storage = StorageFactory.create(StorageType.MEMORY)
    service = PlaybookService(storage)
    print("✅ Storage created")
    print()

    # 2. Load playbooks
    print("📚 Loading playbooks...")
    playbooks_dir = Path(__file__).parent.parent / "playbooks"
    count = await load_default_playbooks(service, playbooks_dir)
    print(f"✅ Loaded {count} playbooks")
    print()

    # 3. List all available playbooks
    print("📋 Available playbooks:")
    titles = await service.list_playbooks()
    for i, title in enumerate(titles, 1):
        print(f"  {i}. {title}")
    print()

    # 4. Query for a specific topic
    questions = [
        "How do I get sunset times?",
        "Show me weather forecast",
        "What about current weather?",
    ]

    for question in questions:
        print(f"🔍 Query: '{question}'")
        results = await service.query_playbooks(question, top_k=1)

        if results:
            playbook = results[0]
            print(f"✅ Found: {playbook.metadata.title}")
            print(f"   Tags: {', '.join(playbook.metadata.tags)}")
            print(f"   Description: {playbook.metadata.description[:80]}...")
        else:
            print("❌ No results found")
        print()

    # 5. Get full playbook content
    print("📖 Getting full playbook content...")
    playbook = await service.get_playbook("Get Sunset and Sunrise Times")
    if playbook:
        print(f"✅ Retrieved: {playbook.metadata.title}")
        print(f"   Content length: {len(playbook.content)} characters")
        print()
        print("   First 300 characters:")
        print("   " + "-" * 66)
        print("   " + playbook.content[:300].replace("\n", "\n   "))
        print("   " + "-" * 66)
    print()

    # 6. Get statistics
    stats = await service.get_stats()
    print(f"📊 Statistics: {stats}")
    print()

    print("✅ Example complete!")


if __name__ == "__main__":
    asyncio.run(main())
