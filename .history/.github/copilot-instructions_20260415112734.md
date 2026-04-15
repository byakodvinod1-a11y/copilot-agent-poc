When reviewing code:

- Flag security issues (SQL injection, hardcoded values).
- Check input validation and null safety.
- Flag bad exception handling (do not swallow exceptions).
- Suggest proper logging.
- Suggest unit tests for edge cases.
- Prefer clean architecture (no business logic in controllers).

Review style:
- Be concise
- Prioritize high severity issues
- Suggest fixes