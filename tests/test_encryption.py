import unittest
import os
from src.encrypt import encrypt_file
from src.decrypt import decrypt_file

class TestFileEncryption(unittest.TestCase):
    def setUp(self):
        # Get absolute paths properly
        self.tests_folder = os.path.abspath("tests")  # Correct path to `tests/`
        self.test_file = os.path.join(self.tests_folder, "test.txt")
        self.encrypted_file = os.path.join(self.tests_folder, "test.txt.enc")

        # Ensure the tests folder exists
        os.makedirs(self.tests_folder, exist_ok=True)

        # Create a test file
        with open(self.test_file, "w") as f:
            f.write("Hello, this is a test.")

    def test_encryption(self):
        encrypt_file(self.test_file)  # Use full path, not "tests/test.txt"
        print(f"Checking if '{self.encrypted_file}' exists…")
        self.assertTrue(os.path.exists(self.encrypted_file))

    def test_decryption(self):
        decrypt_file(self.encrypted_file)
        print(f"Checking if '{self.test_file}' exists after decryption…")
        self.assertTrue(os.path.exists(self.test_file))

    def tearDown(self):
        # Remove files after testing
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.encrypted_file):
            os.remove(self.encrypted_file)

if __name__ == "__main__":
    unittest.main()
