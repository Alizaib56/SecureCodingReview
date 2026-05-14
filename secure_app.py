# ==========================================
# Secure Login System
# CodeAlpha - Secure Coding Review
# ==========================================

import hashlib

print("=== Secure Login System ===")

# Secure stored username
stored_username = "admin"

# Strong password
stored_password = "StrongPassword123!"

# Convert password into SHA-256 hash
stored_password_hash = hashlib.sha256(
    stored_password.encode()
).hexdigest()

# User input
username = input("Enter Username: ")
password = input("Enter Password: ")

# Convert entered password into hash
entered_password_hash = hashlib.sha256(
    password.encode()
).hexdigest()

# Secure authentication
if username == stored_username and entered_password_hash == stored_password_hash:
    print("\n✅ Login Successful")
else:
    print("\n❌ Invalid Credentials")