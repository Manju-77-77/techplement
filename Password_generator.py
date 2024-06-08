import random
import string


def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):

    char_pool = ''

    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("At least one character type must be selected")

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password


# Example usage
password_length = int(input("ENTER PASSWORD LENGTH :="))
password = generate_password(length=password_length)
print(f"Generated password: {password}")
