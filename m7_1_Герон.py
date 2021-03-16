from math import sqrt
a = int(input('сторона а'))
b = int(input('сторона b'))
c = int(input('сторона c'))


def heron(a, b, c): 
    s=(a+b+c)/2 
    return sqrt(s * (s - a) * (s - b) * (s - c))
    

if a + b > c or b + c > a or a + c > b:
    print("Площадь трегольника со сторонами" ,a ,b, c, " =" ,heron(a,b,c))
else: print("Не правильно заданы стороны")