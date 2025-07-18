import string
import random

chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

cipher_text = input("Enter a message to encrypt:")
plain_text = ""

for letter in cipher_text:
    index =key.index(letter)
    plain_text += chars[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")