import random

letters = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("0123456789")
symbols = list("!@#$%&*()_+")

print("Welcome to the Password Generator 🔐")

num_letters = int(input("How many letters do you want in your password?\n"))
num_numbers = int(input("How many numbers do you want in your password?\n"))
num_symbols = int(input("How many symbols do you want in your password?\n"))

password_list = []

for _ in range(num_letters):
    password_list.append(random.choice(letters))

for _ in range(num_numbers):
    password_list.append(random.choice(numbers))

for _ in range(num_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = "".join(password_list)
print("Your password is:", password)
