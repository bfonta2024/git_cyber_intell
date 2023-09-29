def is_valid_password(password):
    return len(password) >= 8

# Example usage
password = input("Enter a password: ")
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is too short. It should be at least 8 characters long.")
