#!/usr/bin/env python3
"""
Async API Usage Example
========================

This example demonstrates how to:
1. Use the playbook service asynchronously
2. Run multiple queries in parallel
3. Handle concurrent operations efficiently
"""

import asyncio
import time
from pathlib import Path

from chuk_mcp_playbook.services.playbook_service import PlaybookService
from chuk_mcp_playbook.storage.factory import StorageFactory, StorageType
from chuk_mcp_playbook.loader import load_default_playbooks


async def query_and_measure(service: PlaybookService, question: str, query_id: int):
    """Query a playbook and measure the time taken."""
    start = time.perf_counter()
    results = await service.query_playbooks(question, top_k=1)
    elapsed = (time.perf_counter() - start) * 1000  # Convert to milliseconds

    if results:
        return {
            "id": query_id,
            "question": question,
            "result": results[0].metadata.title,
            "time_ms": elapsed,
        }
    return {
        "id": query_id,
        "question": question,
        "result": "No results",
        "time_ms": elapsed,
    }


async def main():
    """Run async API usage example."""
    print("=" * 70)
    print("Example 3: Async API Usage & Concurrent Queries")
    print("=" * 70)
    print()

    # Setup
    storage = StorageFactory.create(StorageType.MEMORY)
    service = PlaybookService(storage)
    playbooks_dir = Path(__file__).parent.parent / "playbooks"
    await load_default_playbooks(service, playbooks_dir)
    print("✅ Setup complete")
    print()

    # Example 1: Sequential queries
    print("🔄 Running 5 queries SEQUENTIALLY...")
    questions = [
        "sunset times",
        "weather forecast",
        "current weather",
        "sunrise data",
        "temperature information",
    ]

    start_time = time.perf_counter()
    sequential_results = []
    for i, question in enumerate(questions, 1):
        result = await query_and_measure(service, question, i)
        sequential_results.append(result)
    sequential_time = (time.perf_counter() - start_time) * 1000

    print(f"✅ Sequential execution completed in {sequential_time:.2f}ms")
    for result in sequential_results:
        print(f"   {result['id']}. '{result['question']}' → {result['result']} ({result['time_ms']:.2f}ms)")
    print()

    # Example 2: Concurrent queries (faster!)
    print("⚡ Running 5 queries CONCURRENTLY...")
    start_time = time.perf_counter()

    # Create tasks for concurrent execution
    tasks = [
        query_and_measure(service, question, i)
        for i, question in enumerate(questions, 1)
    ]

    # Run all tasks concurrently
    concurrent_results = await asyncio.gather(*tasks)
    concurrent_time = (time.perf_counter() - start_time) * 1000

    print(f"✅ Concurrent execution completed in {concurrent_time:.2f}ms")
    for result in concurrent_results:
        print(f"   {result['id']}. '{result['question']}' → {result['result']} ({result['time_ms']:.2f}ms)")
    print()

    # Performance comparison
    speedup = sequential_time / concurrent_time
    print(f"📊 Performance Comparison:")
    print(f"   Sequential: {sequential_time:.2f}ms")
    print(f"   Concurrent: {concurrent_time:.2f}ms")
    print(f"   Speedup: {speedup:.2f}x faster")
    print()

    # Example 3: Concurrent operations of different types
    print("🔀 Running MIXED concurrent operations...")
    start_time = time.perf_counter()

    mixed_tasks = [
        service.query_playbooks("weather", top_k=2),
        service.list_playbooks(),
        service.get_stats(),
        service.get_playbook("Get Sunset and Sunrise Times"),
        service.query_playbooks("forecast", top_k=1),
    ]

    results = await asyncio.gather(*mixed_tasks)
    mixed_time = (time.perf_counter() - start_time) * 1000

    print(f"✅ Mixed operations completed in {mixed_time:.2f}ms")
    print(f"   Query 1: Found {len(results[0])} playbooks")
    print(f"   List: {len(results[1])} total playbooks")
    print(f"   Stats: {results[2]}")
    print(f"   Get: {'Found' if results[3] else 'Not found'}")
    print(f"   Query 2: Found {len(results[4])} playbooks")
    print()

    # Example 4: Error handling with async
    print("⚠️  Demonstrating async error handling...")
    try:
        tasks = [
            service.get_playbook("Valid Playbook"),  # Will fail
            service.get_playbook("Get Sunset and Sunrise Times"),  # Will succeed
            service.query_playbooks("weather"),  # Will succeed
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for i, result in enumerate(results, 1):
            if isinstance(result, Exception):
                print(f"   Task {i}: ❌ Error - {result}")
            elif result is None:
                print(f"   Task {i}: ⚠️  No result")
            else:
                print(f"   Task {i}: ✅ Success")
    except Exception as e:
        print(f"   Error: {e}")
    print()

    print("✅ Example complete!")


if __name__ == "__main__":
    asyncio.run(main())
