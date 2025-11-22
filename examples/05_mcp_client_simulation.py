#!/usr/bin/env python3
"""
MCP Client Simulation Example
==============================

This example simulates how an MCP client (like Claude Desktop or chuk-ai-planner)
would interact with the playbook server to:
1. Query for playbooks
2. Parse the returned playbook
3. Extract MCP tools and parameters
4. Execute the playbook steps
"""

import asyncio
import re
from pathlib import Path

from chuk_mcp_playbook.services.playbook_service import PlaybookService
from chuk_mcp_playbook.storage.factory import StorageFactory, StorageType
from chuk_mcp_playbook.loader import load_default_playbooks


def parse_playbook(content: str) -> dict:
    """
    Parse a playbook to extract structured information.

    This simulates what an AI planner would do.
    """
    sections = {}
    current_section = None
    current_content = []

    for line in content.split("\n"):
        # Check for main sections
        if line.startswith("## "):
            # Save previous section
            if current_section:
                sections[current_section] = "\n".join(current_content).strip()
            current_section = line[3:].strip()
            current_content = []
        else:
            current_content.append(line)

    # Save last section
    if current_section:
        sections[current_section] = "\n".join(current_content).strip()

    return sections


def extract_steps(sections: dict) -> list[str]:
    """Extract step-by-step instructions from playbook."""
    if "Steps" not in sections:
        return []

    steps_text = sections["Steps"]
    steps = []

    for line in steps_text.split("\n"):
        # Look for numbered steps
        match = re.match(r"^\d+\.\s+(.+)$", line.strip())
        if match:
            steps.append(match.group(1))

    return steps


def extract_mcp_tools(sections: dict) -> list[dict]:
    """Extract MCP tools and their parameters from playbook."""
    if "MCP Tools Required" not in sections:
        return []

    tools_text = sections["MCP Tools Required"]
    tools = []
    current_tool = None

    for line in tools_text.split("\n"):
        # Check for server name (### header)
        if line.startswith("### "):
            if current_tool:
                tools.append(current_tool)
            current_tool = {"server": line[4:].strip(), "tool": None, "parameters": []}

        # Check for tool name
        elif "**Tool**:" in line:
            tool_name = line.split("**Tool**:")[1].strip().strip("`")
            if current_tool:
                current_tool["tool"] = tool_name

        # Check for parameters
        elif line.strip().startswith("- `") and current_tool:
            # Extract parameter name and details
            param_match = re.match(r"^\s*-\s*`([^`]+)`\s*\(([^)]+)\):\s*(.+)$", line.strip())
            if param_match:
                param_name = param_match.group(1)
                param_type = param_match.group(2)
                param_desc = param_match.group(3)
                current_tool["parameters"].append({
                    "name": param_name,
                    "type": param_type,
                    "description": param_desc,
                })

    if current_tool:
        tools.append(current_tool)

    return tools


async def simulate_planner_execution(playbook_content: str, user_question: str):
    """
    Simulate how an AI planner would execute a playbook.

    This shows the complete workflow:
    1. Parse the playbook
    2. Extract steps and tools
    3. Plan execution
    4. Simulate tool calls
    """
    print(f"🎯 User Question: '{user_question}'")
    print()

    # Parse playbook
    print("📖 Parsing playbook...")
    sections = parse_playbook(playbook_content)
    print(f"✅ Found {len(sections)} sections")
    print()

    # Extract steps
    print("📝 Extracting steps...")
    steps = extract_steps(sections)
    for i, step in enumerate(steps, 1):
        print(f"  {i}. {step}")
    print()

    # Extract MCP tools
    print("🔧 Extracting required MCP tools...")
    tools = extract_mcp_tools(sections)
    for tool_info in tools:
        print(f"  Server: {tool_info['server']}")
        print(f"  Tool: {tool_info['tool']}")
        if tool_info['parameters']:
            print(f"  Parameters:")
            for param in tool_info['parameters']:
                print(f"    - {param['name']} ({param['type']}): {param['description']}")
        print()

    # Simulate execution plan
    print("🚀 Creating execution plan...")
    print("  Plan:")
    print("  1. Parse user input to extract parameters")
    print(f"  2. Call {tools[0]['server']}.{tools[0]['tool']} with extracted parameters")
    print("  3. Parse response and format output")
    print("  4. Return result to user")
    print()

    # Simulate tool call
    print("🎬 Simulating MCP tool call...")
    print(f"  Calling: {tools[0]['server']}.{tools[0]['tool']}")
    print(f"  Parameters: {[p['name'] for p in tools[0]['parameters']]}")
    print()

    # Simulate response
    print("📬 Simulated response:")
    if "Example Output" in sections:
        print("  " + sections["Example Output"][:200].replace("\n", "\n  "))
    print()


async def main():
    """Run MCP client simulation example."""
    print("=" * 70)
    print("Example 5: MCP Client Simulation (AI Planner Workflow)")
    print("=" * 70)
    print()

    # Setup
    storage = StorageFactory.create(StorageType.MEMORY)
    service = PlaybookService(storage)
    playbooks_dir = Path(__file__).parent.parent / "playbooks"
    count = await load_default_playbooks(service, playbooks_dir)
    print(f"✅ Loaded {count} playbooks")
    print()

    # Scenario 1: Query for sunset times
    print("=" * 70)
    print("Scenario 1: User asks about sunset times")
    print("=" * 70)
    print()

    user_question = "What time is sunset in London today?"
    print(f"❓ User: '{user_question}'")
    print()

    # Planner queries playbook server
    print("🔍 Planner queries playbook repository...")
    results = await service.query_playbooks("sunset times", top_k=1)

    if not results:
        print("❌ No playbook found!")
        return

    playbook = results[0]
    print(f"✅ Found playbook: '{playbook.metadata.title}'")
    print()

    # Planner processes the playbook
    await simulate_planner_execution(playbook.content, user_question)

    print("=" * 70)
    print()

    # Scenario 2: Query for weather forecast
    print("=" * 70)
    print("Scenario 2: User asks about weather forecast")
    print("=" * 70)
    print()

    user_question2 = "What's the weather forecast for Paris this week?"
    results2 = await service.query_playbooks("weather forecast", top_k=1)

    if results2:
        playbook2 = results2[0]
        print(f"✅ Found playbook: '{playbook2.metadata.title}'")
        print()
        await simulate_planner_execution(playbook2.content, user_question2)

    print("✅ Example complete!")
    print()
    print("💡 Key Insights:")
    print("  - Playbooks are queryable with natural language")
    print("  - Returned markdown is parseable by LLMs")
    print("  - Steps are in plain English (not code)")
    print("  - MCP tools are clearly specified with parameters")
    print("  - AI planners can extract and execute the workflow")


if __name__ == "__main__":
    asyncio.run(main())
