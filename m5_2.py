# определяем все делители числа
n = int(input("Введите число: "))
i = 1
while i<= n//2:
    if n//i == n/i:
        print("Делитель: ", i)
    i+=1
print("Делитель: ", n)
