import random
import string

print("Password Generator")
length = int(input("Enter the length of the password: "))
characters = string.ascii_letters + string.digits
password = ""

for i in range(length):
    password += random.choice(characters)
print("Your generated password is: " )
print(password)    