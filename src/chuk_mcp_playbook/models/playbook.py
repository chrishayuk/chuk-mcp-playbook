"""Playbook domain models using Pydantic."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PlaybookMetadata(BaseModel):
    """Metadata for a playbook."""

    title: str = Field(..., description="Title of the playbook")
    description: str = Field(..., description="Brief description of what this playbook does")
    tags: list[str] = Field(default_factory=list, description="Tags for categorization")
    author: Optional[str] = Field(None, description="Author of the playbook")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update timestamp")


class Playbook(BaseModel):
    """Complete playbook with content and metadata."""

    metadata: PlaybookMetadata = Field(..., description="Playbook metadata")
    content: str = Field(..., description="Markdown content of the playbook")

    def matches_query(self, query: str) -> tuple[bool, float]:
        """
        Check if this playbook matches the query.
        Returns (matches, relevance_score) where score is 0-1.

        Uses word-based matching for better results with natural language queries.
        """
        query_lower = query.lower()

        # Extract meaningful words from query (skip common words)
        stop_words = {'how', 'do', 'i', 'get', 'the', 'a', 'an', 'is', 'are', 'what', 'show', 'me', 'about'}
        query_words = [word for word in query_lower.split() if word not in stop_words and len(word) > 2]

        if not query_words:
            # Fallback to original query if all words were filtered
            query_words = query_lower.split()

        score = 0.0
        title_lower = self.metadata.title.lower()
        desc_lower = self.metadata.description.lower()
        content_lower = self.content.lower()

        # Check each query word
        for word in query_words:
            word_score = 0.0

            # Title match (highest weight)
            if word in title_lower:
                word_score += 0.5

            # Tag matches
            for tag in self.metadata.tags:
                if word in tag.lower():
                    word_score += 0.3
                    break

            # Description match
            if word in desc_lower:
                word_score += 0.2

            # Content match (lowest weight)
            if word in content_lower:
                word_score += 0.1

            score += word_score

        # Normalize by number of query words to keep score in reasonable range
        if query_words:
            score = score / len(query_words)

        return (score > 0, min(score, 1.0))


class PlaybookQuery(BaseModel):
    """Query parameters for searching playbooks."""

    question: str = Field(..., description="Natural language question to search for")
    top_k: int = Field(default=3, ge=1, le=10, description="Maximum number of results to return")
    tags: Optional[list[str]] = Field(None, description="Filter by specific tags")
