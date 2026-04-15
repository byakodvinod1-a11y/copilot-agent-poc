# Copilot Review Instructions

When reviewing code in this repository:

## Core Priorities
- Security (SQL injection, hardcoded secrets, unsafe input handling)
- Input validation and null safety
- Proper exception handling (do not swallow exceptions)
- Logging and observability
- Code readability and maintainability

## Review Rules

1. Flag any SQL injection risks or unsafe query construction.
2. Flag missing validation for inputs (null, empty, malformed).
3. Flag poor exception handling:
   - Catching generic Exception
   - Returning generic values instead of propagating errors
4. Suggest proper logging for failures.
5. Suggest improvements for clean and maintainable code.
6. Suggest unit tests for:
   - Happy path
   - Invalid input
   - Error scenarios

## Output Format

For each issue, provide:

- Title
- Severity (High / Medium / Low)
- Violated Rule
- Explanation
- Suggested Fix
- Recommended Tests

## Important

- Be concise and actionable.
- Prioritize high severity issues first.
- Always suggest concrete fixes.