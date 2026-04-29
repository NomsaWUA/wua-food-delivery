import re
import hashlib

def hash_password(password):
    """Hash a password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(name, email, student_id, password):
    """
    Register a new user.
    Args: name, email, student_id, password
    """
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email format")
        return
    hashed = hash_password(password)
    print(f"Registering {name} with email {email}")

def login_user(email, password):
    """
    Login a user.
    Args: email, password
    """
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email format")
        return
    hashed = hash_password(password)
    print(f"Logging in {email}")
