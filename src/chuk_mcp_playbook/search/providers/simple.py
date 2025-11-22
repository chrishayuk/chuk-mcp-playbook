"""Simple substring-based search."""

from chuk_mcp_playbook.models.playbook import Playbook
from chuk_mcp_playbook.search.base import SearchProvider


class SimpleSearch(SearchProvider):
    """
    Simple substring-based search provider.

    Features:
    - Direct substring matching
    - Case-insensitive
    - Weighted scoring (title > tags > description > content)
    - Fast and straightforward
    """

    def score(self, playbook: Playbook, query: str) -> tuple[bool, float]:
        """
        Score playbook using simple substring matching.

        Returns:
            Tuple of (matches, score) where score is 0.0-1.0
        """
        query_lower = query.lower()
        score = 0.0

        # Title match (highest weight)
        if query_lower in playbook.metadata.title.lower():
            score += 0.5

        # Tag matches
        for tag in playbook.metadata.tags:
            if query_lower in tag.lower():
                score += 0.3
                break

        # Description match
        if query_lower in playbook.metadata.description.lower():
            score += 0.2

        # Content match (lowest weight)
        if query_lower in playbook.content.lower():
            score += 0.1

        return (score > 0, min(score, 1.0))
