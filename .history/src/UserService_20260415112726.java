public class UserService {

    public String createUser(String email) {
        try {
            if (email == null) return null;

            // BAD: no validation
            String query = "INSERT INTO users VALUES ('" + email + "')"; // SQL injection

            // BAD: no logging, no proper exception handling
            return "success";

        } catch (Exception e) {
            return "error"; // swallowing exception
        }
    }
}