import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

class UserServiceTest {

    private final UserService userService = new UserService();

    @Test
    void createUser_shouldThrowForNullEmail() {
        assertThrows(IllegalArgumentException.class, () -> userService.createUser(null));
    }

    @Test
    void createUser_shouldThrowForInvalidEmail() {
        assertThrows(IllegalArgumentException.class, () -> userService.createUser("bad-email"));
    }

    @Test
    void createUser_shouldReturnSuccessForValidEmail() {
        assertEquals("success", userService.createUser("user@example.com"));
    }
}