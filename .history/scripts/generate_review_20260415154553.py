from pathlib import Path


def main() -> None:
    instructions_path = Path(".github/copilot-instructions.md")
    source_candidates = [
        Path("src/main/java/com/example/service/UserService.java"),
        Path("src/UserService.java"),
    ]

    if not instructions_path.exists():
        raise FileNotFoundError(f"Missing instructions file: {instructions_path}")

    instructions = instructions_path.read_text(encoding="utf-8")

    source_path = next((p for p in source_candidates if p.exists()), None)
    if source_path is None:
        raise FileNotFoundError("Could not find UserService.java in expected locations.")

    source = source_path.read_text(encoding="utf-8")

    reviews_dir = Path("reviews")
    reviews_dir.mkdir(exist_ok=True)

    review = f"""# UserService Review

## Summary
`{source_path.as_posix()}` was reviewed against `.github/copilot-instructions.md`.

## Findings

### Issue 1: Input validation
- Severity: Medium
- Violated Rule: Check input validation and null safety.
- Explanation: The service should reject null, blank, and malformed emails clearly.
- Suggested Fix: Use explicit validation and fail fast with `IllegalArgumentException`.

### Issue 2: Maintainability
- Severity: Low
- Violated Rule: Suggest improvements for clean and maintainable code.
- Explanation: Keep logic simple and aligned with the current POC scope.
- Suggested Fix: Use a small, testable implementation and clear package structure.

## Reviewed Instructions

{instructions}

## Reviewed Source

{source}
"""
