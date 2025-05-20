import hashlib

def get_sha256_hash(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        return hashlib.sha256(data).hexdigest()

hash1 = get_sha256_hash("gasnica.bmp")
hash2 = get_sha256_hash("gasnica-zmieniona.bmp")

print(f"SHA-256 gasnica.bmp: {hash1}")
print(f"SHA-256 gasnica-zmieniona.bmp: {hash2}")
