# Secure File Encryption Tool

A command-line tool written in Python that encrypts and decrypts files
using symmetric encryption (Fernet from the `cryptography` library:
AES-128-CBC with HMAC-SHA256).

## Features
- Generate and save a secret key (refuses to overwrite an existing key)
- Encrypt any file
- Decrypt files using the saved key

## Usage
pip install cryptography
python tool.py

## Notes
Keep `secret.key` private. Without it, encrypted files cannot be recovered.