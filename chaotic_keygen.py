import hashlib

def chaotic_key(seed: float, length: int = 32) -> bytes:
    r = 3.999
    x = seed % 1
    key = bytearray()
    for _ in range(length):
        x = r * x * (1 - x)
        key.append(int(x * 256) % 256)
    return bytes(key)