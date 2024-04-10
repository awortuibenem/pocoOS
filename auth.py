import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user(username, password, stored_password):
    hashed_password = hash_password(password)
    return hashed_password == stored_password
