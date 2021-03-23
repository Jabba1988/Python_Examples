import random
import string

a = int(input("Кол-во символов в пароле "))

pwd = ""
i = -1
while i < a:
    if i % 2 == 0:
        pwd = pwd + random.choice(string.ascii_letters)
    else:
        pwd = pwd + str(random.randint(0,9))
    i += 1
print(pwd)