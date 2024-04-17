# Python Password Generator

import random
import string


def generate_password(length, level, output=[]):
    chars = string.ascii_letters
    if level > 1:
        chars += string.digits
    if level > 2:
        chars += string.punctuation

    for i in range(length):
        output.append(random.choice(chars))

    return "".join(output)


print(("-" * 30) + "\n Python Password Generator\n" + ("-" * 30))

print("Password Difficulty Levels:")
print("1 - Letters (upper and lower case)")
print("2 - Letters and numbers")
print("3 - Letters, numbers, and special characters")

level = int(input("Choose Difficulty Level (1/2/3): "))

if level not in [1, 2, 3]:
    print("Invalid difficulty level! Defaulting to level 1.")
    level = 1

password_length = int(input("Enter Password Length: "))

generated_password = generate_password(password_length, level)
print("Generated Password:", generated_password)





