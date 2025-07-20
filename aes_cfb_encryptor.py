from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt(data: bytes, key: bytes) -> bytes:
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return iv + cipher.encrypt(data)

def decrypt(ciphertext: bytes, key: bytes) -> bytes:
    iv = ciphertext[:16]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.decrypt(ciphertext[16:])