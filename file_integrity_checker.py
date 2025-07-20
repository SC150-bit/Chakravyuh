import hashlib

def file_hash(path):
    h = hashlib.sha512()
    with open(path, 'rb') as f:
        chunk = f.read(8192)
        while chunk:
            h.update(chunk)
            chunk = f.read(8192)
    return h.hexdigest()