from pathlib import Path

instructions = Path(".github/copilot-instructions.md").read_text(encoding="utf-8")
source = Path("src/UserService.java").read_text(encoding="utf-8")

reviews_dir = Path("reviews")
reviews_dir.mkdir(exist_ok=True)

review = """# UserService Review

## Summary
`src/UserService.java` violates repository review guidance by using unsafe SQL concatenation, weak input validation, swallowed exceptions, and missing logging.

## Findings

### Issue 1: SQL injection risk
- Severity: High
- Violated Rule: Flag any SQL injection risks or unsafe query construction.
- Explanation: SQL is constructed through string concatenation with user-controlled input.
- Suggested Fix: Use `PreparedStatement` with parameter binding.
- Recommended Tests:
  - verify valid email insert path
  - verify unsafe input is not concatenated into SQL

### Issue 2: Missing validation and null safety
- Severity: High
- Violated Rule: Flag missing validation for inputs (null, empty, malformed).
- Explanation: The method only checks null and does not validate blank or malformed emails.
- Suggested Fix: Fail fast with explicit validation using `IllegalArgumentException`.
- Recommended Tests:
  - null input
  - blank input
  - malformed email

### Issue 3: Swallowed exceptions
- Severity: High
- Violated Rule: Flag poor exception handling.
- Explanation: The code catches generic `Exception` and returns a generic error value.
- Suggested Fix: Log the exception and throw a domain/service exception.
- Recommended Tests:
  - database failure path
  - exception propagation
"""

fixes = """# UserService Fix Suggestions

## Corrected Code

```java
import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Objects;
import java.util.logging.Level;
import java.util.logging.Logger;

public class UserService {

    private static final Logger LOGGER = Logger.getLogger(UserService.class.getName());
    private final DataSource dataSource;

    public UserService(DataSource dataSource) {
        this.dataSource = Objects.requireNonNull(dataSource, "dataSource must not be null");
    }

    public String createUser(String email) {
        validateEmail(email);

        String sql = "INSERT INTO users(email) VALUES (?)";

        try (Connection connection = dataSource.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {

            statement.setString(1, email);
            int updated = statement.executeUpdate();

            if (updated != 1) {
                throw new UserServiceException("Unexpected row count while creating user");
            }

            return "success";
        } catch (SQLException ex) {
            LOGGER.log(Level.SEVERE, "Failed to create user", ex);
            throw new UserServiceException("Unable to create user", ex);
        }
    }

    private void validateEmail(String email) {
        if (email == null || email.isBlank()) {
            throw new IllegalArgumentException("email must not be null or blank");
        }

        if (!email.matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$")) {
            throw new IllegalArgumentException("email format is invalid");
        }
    }
}