package com.example.service;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class UserServiceTest {

    private final UserService userService = new UserService();

    @Test
    void createUser_shouldThrowForNullEmail() {
        assertThrows(IllegalArgumentException.class,
            () -> userService.createUser(null));
    }
}