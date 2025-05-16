from cryptography.fernet import Fernet
import os

KEY_PATH = os.path.join(os.path.dirname(__file__), "../keys/key.key")

# loads encryption key
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Moves one level up
KEY_PATH = os.path.join(BASE_DIR, "keys", "key.key")  # Correctly defines keys path

def load_or_generate_key():
    if not os.path.exists(KEY_PATH):
        key = Fernet.generate_key()
        with open(KEY_PATH, "wb") as key_file:
            key_file.write(key)
    with open(KEY_PATH, "rb") as key_file:
        return key_file.read()

def load_key():
    if not os.path.exists(KEY_PATH):
        raise FileNotFoundError("Encryption key not found! Run encrypt.py first to generate a key.")
    with open(KEY_PATH, "rb") as key_file:
        return key_file.read()

# decrypts file
def decrypt_file(encrypted_file_name):
    key = load_key()
    cipher = Fernet(key)

    # Define correct path to encrypted file
    encrypted_file_path = os.path.join(os.getcwd(), "tests", encrypted_file_name)

    if not os.path.exists(encrypted_file_path):
        print(f"Error: Encrypted file '{encrypted_file_path}' not found!")
        return

    with open(encrypted_file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    original_file_path = encrypted_file_path.replace(".enc", "")

    with open(original_file_path, "wb") as file:
        file.write(decrypted_data)

    print(f"File '{original_file_path}' decrypted successfully!")

# runs decryption
if __name__ == "__main__":
    encrypted_file = input("Enter the encrypted file name: ")
    decrypt_file(encrypted_file)
