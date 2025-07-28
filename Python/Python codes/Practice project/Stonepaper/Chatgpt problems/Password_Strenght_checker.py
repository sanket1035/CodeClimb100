password = input("Enter your password: ")

if len(password) < 8:
    print("❌ Password too short (must be at least 8 characters)")

has_upper = any(ch.isupper() for ch in password)
has_lower = any(ch.islower() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_special = any(ch in "!@#$%^&*()" for ch in password)

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("✅ Strong Password")
else:
    print("❌ Weak Password – Missing:")
    if not has_upper:
        print("- At least one uppercase letter")
    if not has_lower:
        print("- At least one lowercase letter")
    if not has_digit:
        print("- At least one digit")
    if not has_special:
        print("- At least one special character (!@#$%^&*())")
