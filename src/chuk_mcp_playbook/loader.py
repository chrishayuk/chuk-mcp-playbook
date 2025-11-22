"""Utility to load playbooks from markdown files."""

import asyncio
import sys
from pathlib import Path
from typing import Optional

from chuk_mcp_playbook.models.playbook import PlaybookMetadata
from chuk_mcp_playbook.services.playbook_service import PlaybookService


class PlaybookLoader:
    """Loads playbooks from markdown files into storage."""

    def __init__(self, service: PlaybookService):
        self.service = service

    def _extract_metadata_from_markdown(self, content: str, filename: str) -> tuple[str, str, list[str]]:
        """
        Extract title, description, and tags from markdown content.

        Returns:
            Tuple of (title, description, tags)
        """
        lines = content.split("\n")
        title = ""
        description = ""
        tags = []

        # Extract title (first # heading)
        for line in lines:
            if line.startswith("# "):
                # Remove "# " and extract title
                full_title = line[2:].strip()
                # If it starts with "Playbook:", extract the actual title
                if full_title.startswith("Playbook:"):
                    title = full_title[9:].strip()
                else:
                    title = full_title
                break

        # Extract description (text after ## Description)
        in_description = False
        for line in lines:
            if line.startswith("## Description"):
                in_description = True
                continue
            if in_description:
                if line.startswith("##"):  # Next section
                    break
                if line.strip():
                    description = line.strip()
                    break

        # Extract tags from filename (e.g., "get_weather_forecast" -> ["weather", "forecast"])
        filename_parts = Path(filename).stem.split("_")
        tags = [part for part in filename_parts if len(part) > 2]

        # Default title from filename if not found
        if not title:
            title = " ".join(word.capitalize() for word in filename_parts)

        # Default description if not found
        if not description:
            description = f"Playbook for {title}"

        return title, description, tags

    async def load_from_file(self, file_path: Path, author: Optional[str] = None) -> None:
        """Load a single playbook from a markdown file."""
        if not file_path.exists():
            raise FileNotFoundError(f"Playbook file not found: {file_path}")

        content = file_path.read_text(encoding="utf-8")
        title, description, tags = self._extract_metadata_from_markdown(content, file_path.name)

        await self.service.create_playbook(
            title=title,
            content=content,
            description=description,
            tags=tags,
            author=author,
        )

    async def load_from_directory(self, directory: Path, author: Optional[str] = None) -> int:
        """
        Load all markdown playbooks from a directory.

        Returns:
            Number of playbooks loaded
        """
        if not directory.exists():
            raise FileNotFoundError(f"Directory not found: {directory}")

        markdown_files = list(directory.glob("*.md"))
        count = 0

        for file_path in markdown_files:
            try:
                await self.load_from_file(file_path, author=author)
                count += 1
            except Exception as e:
                print(f"Error loading {file_path.name}: {e}", file=sys.stderr)

        return count


async def load_default_playbooks(service: PlaybookService, playbooks_dir: Optional[Path] = None) -> int:
    """
    Load default playbooks from the playbooks directory.

    Args:
        service: PlaybookService instance
        playbooks_dir: Optional custom playbooks directory path

    Returns:
        Number of playbooks loaded
    """
    if playbooks_dir is None:
        # Default to playbooks/ directory relative to project root
        # __file__ is src/chuk_mcp_playbook/loader.py
        # parent -> src/chuk_mcp_playbook
        # parent.parent -> src
        # parent.parent.parent -> project root
        current_file = Path(__file__)
        project_root = current_file.parent.parent.parent
        playbooks_dir = project_root / "playbooks"

    if not playbooks_dir.exists():
        print(f"Playbooks directory not found: {playbooks_dir}", file=sys.stderr)
        return 0

    loader = PlaybookLoader(service)
    count = await loader.load_from_directory(playbooks_dir, author="Chuk AI")
    # Only log to stderr to avoid polluting STDIO transport
    print(f"Loaded {count} playbooks from {playbooks_dir}", file=sys.stderr)
    return count
