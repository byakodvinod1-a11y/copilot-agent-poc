package main.java;
public class UserService {

    public String createUser(String email) {
        if (email == null || email.isBlank()) {
            throw new IllegalArgumentException("email must not be null or blank");
        }
        if (!email.contains("@")) {
            throw new IllegalArgumentException("invalid email");
        }
        return "success";
    }
}