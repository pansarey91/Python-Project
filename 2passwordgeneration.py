# import string
# import random

# def generate_password():

#     #this function generates a random password in first way
#     # length = int(input("Enter the length of the password: "))
#     # characters = string.ascii_letters + string.digits + string.punctuation
#     # password = "".join(random.choice(characters) for _ in range(length))
#     # print("Generated Password:", password)

#     #this function generates a random password in second way

#     length = int(input("Enter the length of the password: "))
#     s1=string.ascii_lowercase
#     s2=string.ascii_uppercase
#     s3=string.digits
#     s4=string.punctuation
#     s=[]
#     s.extend(list(s1))
#     s.extend(list(s2))
#     s.extend(list(s3))
#     s.extend(list(s4))
#     random.shuffle(s)
#     print("".join(s[0:length]))

# generate_password()

import string
import random

length = int(input("Enter the length of the password: "))
password = []

# At least one lowercase letter
password.append(random.choice(string.ascii_lowercase))

# At least one uppercase letter
password.append(random.choice(string.ascii_uppercase))

# At least one digit
password.append(random.choice(string.digits))

# At least one symbol
password.append(random.choice(string.punctuation))

# Fill the remaining length with random characters
for _ in range(length - 4):
    password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

# Shuffle the password
random.shuffle(password)

# Convert the list to a string and print the password
print("".join(password))
