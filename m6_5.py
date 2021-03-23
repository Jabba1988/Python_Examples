import random

q = random.randint(1, 100)
attempts = int(0)
print("Привет я загадал число от 1 до 100, угадай его")
a = int(input('Число: '))

while True:
    if a < q:
        print("Я загадал большее число")
        attempts += 1
    elif a == q:
        print("угадал, кол-во попыток: ", attempts)
        break
    else:
        print("Я загадал число поменьше")
        attempts += 1
    a = int(input('Число : '))