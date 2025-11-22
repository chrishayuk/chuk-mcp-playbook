"""Keyword-based search with stop word filtering."""

from chuk_mcp_playbook.models.playbook import Playbook
from chuk_mcp_playbook.search.base import SearchProvider


class KeywordSearch(SearchProvider):
    """
    Keyword-based search provider.

    Features:
    - Filters stop words
    - Word-based matching
    - Weighted scoring (title > tags > description > content)
    - Normalized scores
    """

    # Common words to filter out from queries
    STOP_WORDS = {
        'how', 'do', 'i', 'get', 'the', 'a', 'an', 'is', 'are', 'what',
        'show', 'me', 'about', 'can', 'you', 'tell', 'find', 'to', 'for'
    }

    def __init__(self, stop_words: set[str] | None = None):
        """
        Initialize keyword search.

        Args:
            stop_words: Optional custom set of stop words to filter
        """
        self.stop_words = stop_words or self.STOP_WORDS

    def _extract_keywords(self, query: str) -> list[str]:
        """Extract meaningful keywords from query."""
        query_lower = query.lower()

        # Extract words, filtering stop words and short words
        keywords = [
            word for word in query_lower.split()
            if word not in self.stop_words and len(word) > 2
        ]

        # Fallback to all words if everything was filtered
        if not keywords:
            keywords = query_lower.split()

        return keywords

    def score(self, playbook: Playbook, query: str) -> tuple[bool, float]:
        """
        Score playbook using keyword matching.

        Returns:
            Tuple of (matches, score) where score is 0.0-1.0
        """
        keywords = self._extract_keywords(query)

        if not keywords:
            return (False, 0.0)

        total_score = 0.0
        title_lower = playbook.metadata.title.lower()
        desc_lower = playbook.metadata.description.lower()
        content_lower = playbook.content.lower()

        # Check each keyword
        for keyword in keywords:
            word_score = 0.0

            # Title match (highest weight - 0.5)
            if keyword in title_lower:
                word_score += 0.5

            # Tag matches (0.3)
            for tag in playbook.metadata.tags:
                if keyword in tag.lower():
                    word_score += 0.3
                    break

            # Description match (0.2)
            if keyword in desc_lower:
                word_score += 0.2

            # Content match (lowest weight - 0.1)
            if keyword in content_lower:
                word_score += 0.1

            total_score += word_score

        # Normalize by number of keywords
        normalized_score = total_score / len(keywords) if keywords else 0.0

        return (normalized_score > 0, min(normalized_score, 1.0))
