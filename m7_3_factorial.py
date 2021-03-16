n = int(input('Введите число '))

def factorial(n):
    factorial = 1
    if n == 1 :
        return factorial
    else:
        while n > 1:
            factorial *= n
            n -= 1
        return factorial

print ("Факториал числа ", n, factorial(n))