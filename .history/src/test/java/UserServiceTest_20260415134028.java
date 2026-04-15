import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

class UserServiceTest {

    private DataSource dataSource;
    private Connection connection;
    private PreparedStatement statement;
    private UserService userService;

    @BeforeEach
    void setUp() throws Exception {
        dataSource = mock(DataSource.class);
        connection = mock(Connection.class);
        statement = mock(PreparedStatement.class);

        when(dataSource.getConnection()).thenReturn(connection);
        when(connection.prepareStatement("INSERT INTO users(email) VALUES (?)")).thenReturn(statement);

        userService = new UserService(dataSource);
    }

    @Test
    void createUser_shouldThrowForNullEmail() {
        assertThrows(IllegalArgumentException.class, () -> userService.createUser(null));
    }

    @Test
    void createUser_shouldThrowForInvalidEmail() {
        assertThrows(IllegalArgumentException.class, () -> userService.createUser("bad-email"));
    }

    @Test
    void createUser_shouldInsertUserForValidEmail() throws Exception {
        when(statement.executeUpdate()).thenReturn(1);

        String result = userService.createUser("user@example.com");

        assertEquals("success", result);
        verify(statement).setString(1, "user@example.com");
        verify(statement).executeUpdate();
    }

    @Test
    void createUser_shouldWrapSQLException() throws Exception {
        when(statement.executeUpdate()).thenThrow(new SQLException("db error"));

        assertThrows(UserServiceException.class, () -> userService.createUser("user@example.com"));
    }
}