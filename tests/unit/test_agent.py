"""Pull Request Review Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_analyze_diff():
    """Test Analyze a PR diff for issues, risks, and improvements."""
    tools = AgentTools()
    result = await tools.analyze_diff(diff="test", base_branch="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_check_security():
    """Test Scan diff for security vulnerabilities (OWASP Top 10, CWE)."""
    tools = AgentTools()
    result = await tools.check_security(diff="test", language="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_check_performance():
    """Test Identify performance anti-patterns in changed code."""
    tools = AgentTools()
    result = await tools.check_performance(diff="test", language="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_check_test_coverage():
    """Test Verify test coverage for changed code paths."""
    tools = AgentTools()
    result = await tools.check_test_coverage(changed_files="test", test_files="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.pr_review_agent_agent import PrReviewAgentAgent
    agent = PrReviewAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
