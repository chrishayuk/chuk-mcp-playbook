"""Utility to load playbooks from markdown files."""

import asyncio
import re
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

    async def load_from_directory(self, directory: Path, author: Optional[str] = None, recursive: bool = True) -> int:
        """
        Load all markdown playbooks from a directory.

        Args:
            directory: Directory path to load playbooks from
            author: Optional author name for the playbooks
            recursive: If True, scan subdirectories recursively (default: True)

        Returns:
            Number of playbooks loaded
        """
        if not directory.exists():
            raise FileNotFoundError(f"Directory not found: {directory}")

        # Use recursive glob to find all .md files in subdirectories
        pattern = "**/*.md" if recursive else "*.md"
        markdown_files = list(directory.glob(pattern))
        count = 0

        for file_path in markdown_files:
            try:
                await self.load_from_file(file_path, author=author)
                count += 1
            except Exception as e:
                print(f"Error loading {file_path.name}: {e}", file=sys.stderr)

        return count


def parse_index_file(index_path: Path) -> list[str]:
    """
    Parse the index.md file and extract locations to ingest.

    Supported formats:
    - file:///absolute/path/to/directory
    - github:owner/repo
    - https://example.com/path

    Args:
        index_path: Path to the index.md file

    Returns:
        List of location strings to ingest
    """
    if not index_path.exists():
        print(f"Index file not found: {index_path}", file=sys.stderr)
        return []

    content = index_path.read_text(encoding="utf-8")
    locations = []

    # Extract locations from code blocks or plain lines
    # Match patterns like:
    # - file:///path/to/dir
    # - github:owner/repo
    # - https://example.com

    for line in content.split("\n"):
        line = line.strip()

        # Skip empty lines and comments
        if not line or line.startswith("#"):
            continue

        # Match filesystem paths
        if line.startswith("file://"):
            locations.append(line)
        # Match GitHub repos
        elif line.startswith("github:"):
            locations.append(line)
        # Match URLs
        elif line.startswith("http://") or line.startswith("https://"):
            locations.append(line)

    return locations


async def load_default_playbooks(service: PlaybookService, playbooks_dir: Optional[Path] = None) -> int:
    """
    Load default playbooks from locations specified in index.md.

    This function looks for an index.md file in the project root and loads playbooks
    from the locations specified in it. If no index.md is found, it falls back to
    loading from the playbooks/ directory.

    Supported location formats:
    - file:///absolute/path/to/directory - Load from filesystem
    - github:owner/repo - Load from GitHub (not yet implemented)
    - https://example.com/path - Load from URL (not yet implemented)

    Args:
        service: PlaybookService instance
        playbooks_dir: Optional custom playbooks directory path (overrides index.md)

    Returns:
        Number of playbooks loaded
    """
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent
    loader = PlaybookLoader(service)
    total_count = 0

    # If playbooks_dir is explicitly provided, use it (legacy behavior)
    if playbooks_dir is not None:
        if not playbooks_dir.exists():
            print(f"Playbooks directory not found: {playbooks_dir}", file=sys.stderr)
            return 0
        count = await loader.load_from_directory(playbooks_dir, author="Chuk AI", recursive=True)
        print(f"Loaded {count} playbooks from {playbooks_dir} (including subdirectories)", file=sys.stderr)
        return count

    # Look for index.md in project root
    index_path = project_root / "index.md"

    if index_path.exists():
        print(f"Found index.md, loading playbooks from specified locations", file=sys.stderr)
        locations = parse_index_file(index_path)

        for location in locations:
            try:
                if location.startswith("file://"):
                    # Extract path from file:// URL
                    path_str = location[7:]  # Remove "file://"
                    location_path = Path(path_str)

                    if not location_path.exists():
                        print(f"Location not found: {location}", file=sys.stderr)
                        continue

                    # Skip the index.md file itself
                    if location_path.is_file() and location_path.name == "index.md":
                        continue

                    if location_path.is_file():
                        await loader.load_from_file(location_path, author="Chuk AI")
                        total_count += 1
                    elif location_path.is_dir():
                        count = await loader.load_from_directory(location_path, author="Chuk AI", recursive=True)
                        total_count += count
                        print(f"Loaded {count} playbooks from {location_path}", file=sys.stderr)

                elif location.startswith("github:"):
                    print(f"GitHub ingestion not yet implemented: {location}", file=sys.stderr)
                    # TODO: Implement GitHub repository loading

                elif location.startswith("http://") or location.startswith("https://"):
                    print(f"URL ingestion not yet implemented: {location}", file=sys.stderr)
                    # TODO: Implement URL-based loading

            except Exception as e:
                print(f"Error loading from {location}: {e}", file=sys.stderr)

        print(f"Loaded {total_count} total playbooks from index.md locations", file=sys.stderr)
        return total_count

    else:
        # Fallback to default playbooks directory
        print(f"No index.md found, using default playbooks directory", file=sys.stderr)
        playbooks_dir = project_root / "playbooks"

        if not playbooks_dir.exists():
            print(f"Playbooks directory not found: {playbooks_dir}", file=sys.stderr)
            return 0

        count = await loader.load_from_directory(playbooks_dir, author="Chuk AI", recursive=True)
        print(f"Loaded {count} playbooks from {playbooks_dir} (including subdirectories)", file=sys.stderr)
        return count
