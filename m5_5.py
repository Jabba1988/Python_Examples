# Пpогpамма вычисляет cos(x)

print(' ВЫЧИСЛЯЕМ СOS X ');
х = float(input("Значение Х = "))
e = float(input("Точность е = "))
сумма = 1.0
слагаемое = 1.0
n = 1

while abs(слагаемое) > e:
    # вычисляет (2n)!
    факториал = 1
    for i in range(1,2*n+1):
        факториал *=i
    
    слагаемое =(((-1)**n)* (х ** (2*n)))/(факториал)
    сумма +=слагаемое
    
    n +=1

print("COS ", х," = ", сумма)

