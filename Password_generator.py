import random
import string

letters = string.ascii_letters
digits = string.digits
special_char = string.punctuation

passkey=letters+digits+special_char

passkey_length = int(input("Enter the length of the password you want to create :"))

password = ''.join(random.choice(passkey) for _ in range(passkey_length))

print("The Generated password is :",password)
