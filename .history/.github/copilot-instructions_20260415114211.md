When reviewing code in this repository:

- Read these instructions before reviewing any code.
- Create a Markdown review report in the reviews/ folder.
- For each issue, include:
  - title
  - severity
  - violated rule
  - explanation
  - suggested fix
- Prioritize security, validation, null safety, exception handling, and maintainability.
- Suggest unit tests for edge cases and failure paths.
- Keep comments concise and actionable.

For Java code:
- Flag SQL injection risks.
- Flag missing input validation.
- Flag swallowed exceptions.
- Suggest logging and clearer error handling.