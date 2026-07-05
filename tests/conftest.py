"""Test configuration for Pull Request Review Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "pr-review-agent", "category": "Software Engineering"}
