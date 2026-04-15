package com.example.service;

public class UserService {
    public String createUser(String email) {
        if (email == null || email.isBlank()) {
            throw new IllegalArgumentException("email must not be null");
        }
        return "success";
    }
}