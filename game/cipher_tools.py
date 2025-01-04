import base64
from cryptography.fernet import Fernet

# Example cipher tools for encryption and decryption

# Generate a new key for Fernet cipher (can be used once per game or per scroll)
def generate_cipher_key():
    return Fernet.generate_key().decode()

# Encrypt text using a specific key
def encrypt_text(text, key):
    cipher = Fernet(key.encode())
    encrypted_text = cipher.encrypt(text.encode()).decode()
    return encrypted_text

# Decrypt text using a specific key
def decrypt_text(encrypted_text, key):
    try:
        cipher = Fernet(key.encode())
        decrypted_text = cipher.decrypt(encrypted_text.encode()).decode()
        return decrypted_text
    except Exception:
        return None

# Caesar cipher encryption
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

# Caesar cipher decryption
def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# Vigenère cipher encryption
def vigenere_cipher_encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    text_as_int = [ord(i) for i in text]
    for i in range(len(text_as_int)):
        value = (text_as_int[i] + key_as_int[i % key_length]) % 26
        encrypted_text += chr(value + 65)
    return encrypted_text

# Vigenère cipher decryption
def vigenere_cipher_decrypt(text, key):
    decrypted_text = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    text_as_int = [ord(i) for i in text]
    for i in range(len(text_as_int)):
        value = (text_as_int[i] - key_as_int[i % key_length]) % 26
        decrypted_text += chr(value + 65)
    return decrypted_text
