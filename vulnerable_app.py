# ==========================================
# Vulnerable Login System
# CodeAlpha - Secure Coding Review
# ==========================================

print("=== Vulnerable Login System ===")

# User enters credentials
username = input("Enter Username: ")
password = input("Enter Password: ")

# Hardcoded credentials (BAD PRACTICE)
stored_username = "admin"
stored_password = "admin123"

# Authentication check
if username == stored_username and password == stored_password:
    print("\n✅ Login Successful")
else:
    print("\n❌ Invalid Credentials")