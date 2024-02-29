import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_char = string.punctuation
alphabet = set(letters + digits + special_char)

pass_length = int(input("How many characters do you want your password to have? : "))
pass_digits = input("Do you want digits in your password? (y/n): ").lower()
pass_letters = input("Do you want letters in your password? (y/n): ").lower()
pass_special_char = input("Do you want special characters in your password? (y/n): ").lower()

if pass_digits == 'n':
    alphabet = [char for char in alphabet if char not in digits]
elif pass_letters == 'n':
    alphabet = [char for char in alphabet if char not in letters]
elif pass_special_char == 'n':
    alphabet = [char for char in alphabet if char not in special_char]
else:
    pass

pwd = ''

for i in range(pass_length):
    pwd += ''.join(secrets.choice(alphabet))
print("Your password is: ", pwd)
