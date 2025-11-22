"""Abstract base class for search providers."""

from abc import ABC, abstractmethod

from chuk_mcp_playbook.models.playbook import Playbook


class SearchProvider(ABC):
    """Abstract base class for playbook search providers."""

    @abstractmethod
    def score(self, playbook: Playbook, query: str) -> tuple[bool, float]:
        """
        Score a playbook against a query.

        Args:
            playbook: The playbook to score
            query: The search query

        Returns:
            Tuple of (matches: bool, score: float)
            - matches: True if the playbook matches the query
            - score: Relevance score (0.0 to 1.0)
        """
        pass

    def search(self, playbooks: list[Playbook], query: str, top_k: int = 3) -> list[Playbook]:
        """
        Search through playbooks and return top matches.

        Args:
            playbooks: List of playbooks to search
            query: Search query
            top_k: Maximum number of results to return

        Returns:
            List of matching playbooks sorted by relevance
        """
        results = []

        for playbook in playbooks:
            matches, score = self.score(playbook, query)
            if matches:
                results.append((playbook, score))

        # Sort by score descending
        results.sort(key=lambda x: x[1], reverse=True)

        # Return top_k playbooks
        return [playbook for playbook, _ in results[:top_k]]
