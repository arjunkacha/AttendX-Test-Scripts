
import unittest


def login(username, password):
    """Sample login logic for demonstrating test cases."""
    if username == "student01" and password == "AttendX@123":
        return True
    return False


class LoginTests(unittest.TestCase):

    def test_login_with_valid_credentials(self):
        self.assertTrue(login("student01", "AttendX@123"))

    def test_login_with_invalid_password(self):
        self.assertFalse(login("student01", "wrongpassword"))

    def test_login_with_empty_credentials(self):
        self.assertFalse(login("", ""))

    def test_login_with_wrong_username(self):
        self.assertFalse(login("wronguser", "AttendX@123"))


if __name__ == "__main__":
    unittest.main()
