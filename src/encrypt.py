from cryptography.fernet import Fernet
import os

KEY_PATH = os.path.join(os.path.dirname(__file__), "../keys/key.key")

# loads or generates an encryption key
def load_or_generate_key():
    if not os.path.exists(KEY_PATH):
        key = Fernet.generate_key()
        with open(KEY_PATH, "wb") as key_file:
            key_file.write(key)
    with open(KEY_PATH, "rb") as key_file:
        return key_file.read()

def load_key():
    with open(KEY_PATH, "rb") as key_file:
        return key_file.read()

# encrypts file
def encrypt_file(file_name):
    key = load_or_generate_key()
    cipher = Fernet(key)

    # Ensure correct file path
    test_file_path = os.path.join(os.getcwd(), "tests", file_name)  # Explicitly look inside `tests/`

    if not os.path.exists(test_file_path):
        print(f"Error: File '{test_file_path}' not found!")
        return

    with open(test_file_path, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    enc_file_path = test_file_path + ".enc"

    # Debugging statement to verify file location
    print(f"Writing encrypted file to: {enc_file_path}")

    # Write encrypted data to the new file
    with open(enc_file_path, "wb") as file:
        file.write(encrypted_data)

    print(f"File '{file_name}' encrypted successfully!")

# runs encryption
if __name__ == "__main__":
    file_name = input("Enter the file name to encrypt: ")
    encrypt_file(file_name)