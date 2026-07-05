# Pull Request Review Agent Architecture

Automated pull request reviewer that performs deep code analysis including security vulnerability detection, performance anti-pattern identification, test coverage gaps, style violations, and architectural conformance checks with inline review comments.

## Domain Tools

- **analyze_diff**: Analyze a PR diff for issues, risks, and improvements
- **check_security**: Scan diff for security vulnerabilities (OWASP Top 10, CWE)
- **check_performance**: Identify performance anti-patterns in changed code
- **check_test_coverage**: Verify test coverage for changed code paths
- **post_review_comment**: Post an inline review comment on a PR
- **approve_or_request_changes**: Submit final review verdict