import random

lower = "qwertyuiopasdfghjklzxcvbnm"

upper = "QWERTYUIOPASDFGHJKLZXCVBNM"

numbers = '1234567890'

special = "!@#$%^&*()-_+=~`[]{}\|:;?/>.<,"

chars = special + upper + lower + numbers

lenght = int(input("Enter the desired paswword lenght "))

password = ''.join(random.sample(chars, lenght))
print("Your generated passwors is:", password)