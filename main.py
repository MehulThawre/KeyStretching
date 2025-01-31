import hashlib
import os
import string

# When we apply a hash function (like SHA-256) to a string, it generates a binary hash output (which is difficult to read). The hexdigest() method converts this binary hash into a readable hexadecimal string.
salt = os.urandom(16)
def key_stretch(hashed_value, iteration = 100000) -> str:

    hashed_value = salt + hashed_value.encode('utf-8')
    for _ in range(iteration):
        hashed_value = hashlib.sha256(hashed_value).digest()
    return hashed_value.hex()

# def visualize_hash(hashed_value):
#     ascii_chars = string.ascii_letters + string.digits + "!@#$%^&*"
#     visual = "".join(ascii_chars[b % len(ascii_chars)] for b in bytes.fromhex(hashed_value))
#
#     print("\n🔑 Hashed Password in ASCII Art Form:")
#     print("-" * 50)
#     print(visual[:50])  # Display first 50 characters for readability
#     print("-" * 50)

get_value = input("Enter the password you want to hash:")
final_hash = key_stretch(get_value)
print(f"This is the password: {get_value}\nHere is the hashed password: {final_hash}",)
# visualize_hash(final_hash)


