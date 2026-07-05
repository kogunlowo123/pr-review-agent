"""Pull Request Review Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class PRReviewRequest(BaseModel):
    """PRReviewRequest for Pull Request Review Agent."""
    repo_url: str
    pr_number: int
    base_branch: str = 'main'
    review_depth: str = 'standard'


class ReviewComment(BaseModel):
    """ReviewComment for Pull Request Review Agent."""
    file_path: str
    line_number: int
    severity: str
    category: str
    message: str
    suggestion: str | None


class ReviewVerdict(BaseModel):
    """ReviewVerdict for Pull Request Review Agent."""
    pr_number: int
    verdict: str
    summary: str
    critical_count: int
    high_count: int
    comments: list

