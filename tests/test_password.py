import unittest
import string
import sys, os

# Ensure project root is in path so password_generator can be imported
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        """Ensure generated password has correct length"""
        length = 16
        password = generate_password(length)
        self.assertEqual(len(password), length)

    def test_include_lowercase(self):
        """Ensure password contains lowercase letters when enabled"""
        password = generate_password(20, use_lower=True, use_upper=False, use_digits=False, use_symbols=False)
        self.assertTrue(any(c.islower() for c in password))

    def test_exclude_lowercase(self):
        """Ensure password does not contain lowercase letters when disabled"""
        password = generate_password(20, use_lower=False, use_upper=True, use_digits=False, use_symbols=False)
        self.assertFalse(any(c.islower() for c in password))

    def test_include_uppercase(self):
        """Ensure password contains uppercase letters when enabled"""
        password = generate_password(20, use_upper=True, use_digits=False, use_symbols=False)
        self.assertTrue(any(c.isupper() for c in password))

    def test_exclude_uppercase(self):
        """Ensure password does not contain uppercase letters when disabled"""
        password = generate_password(20, use_upper=False, use_digits=False, use_symbols=False)
        self.assertFalse(any(c.isupper() for c in password))

    def test_include_digits(self):
        """Ensure password contains digits when enabled"""
        password = generate_password(20, use_digits=True, use_upper=False, use_symbols=False)
        self.assertTrue(any(c.isdigit() for c in password))

    def test_exclude_digits(self):
        """Ensure password does not contain digits when disabled"""
        password = generate_password(20, use_digits=False, use_upper=False, use_symbols=False)
        self.assertFalse(any(c.isdigit() for c in password))

    def test_include_symbols(self):
        """Ensure password contains symbols when enabled"""
        password = generate_password(20, use_symbols=True, use_upper=False, use_digits=False)
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_exclude_symbols(self):
        """Ensure password does not contain symbols when disabled"""
        password = generate_password(20, use_symbols=False, use_upper=False, use_digits=False)
        self.assertFalse(any(c in string.punctuation for c in password))

    def test_no_character_sets_selected(self):
        """Ensure error is raised if no character sets are selected"""
        with self.assertRaises(ValueError):
            generate_password(10, use_lower=False, use_upper=False, use_digits=False, use_symbols=False)

if __name__ == "__main__":
    unittest.main()
