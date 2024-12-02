import hashlib

def hash_password(password):
    sha256_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return sha256_hash

password = input("Enter the password: ")
hashed_password = hash_password(password)
print("SHA-256 Hashed Password:", hashed_password)

        
