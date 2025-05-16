# **File Encryption Tool**

## **Overview**
The **File Encryption Tool** is a Python-based utility that provides secure encryption and decryption for files using the **Fernet symmetric encryption** method from the `cryptography` library. This tool ensures sensitive data is protected from unauthorized access.

## **Features**
- **File Encryption:** Encrypts files using a generated key.
- **File Decryption:** Decrypts encrypted files back to their original form.
- **Key Management:** Automatically generates and securely stores encryption keys.
- **Error Handling:** Detects and prevents missing file or incorrect key errors.

## **Installation**
### **Prerequisites**
Ensure you have Python installed on your system.  
To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

## **Usage**
### **Encrypting a File**
Run:
```bash
python src/encrypt.py
```
Enter the name of the file you want to encrypt when prompted.

### **Decrypting a File**
Run:
```bash
python src/decrypt.py
```
Enter the name of the encrypted file when prompted.

## **Project Structure**
```
📁 file-encryption-tool/
    ├── 📁 src/                # Contains encryption and decryption logic
    ├── 📁 tests/              # Unit tests for validation
    ├── 📁 keys/               # Stores encryption keys (ignored by Git)
    ├── 📄 requirements.txt    # Python dependencies
    ├── 📄 README.md           # Documentation
```

## **Security Considerations**
- **Keep encryption keys secure.** Never expose `keys/key.key` to public repositories.
- **Use a strong and unique key** for each encryption process when handling highly sensitive data.
- **Regularly update dependencies** to ensure security vulnerabilities are patched.

## **License**
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## **Contributing**
Contributions are welcome!

---

