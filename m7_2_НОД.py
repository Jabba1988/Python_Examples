a = int(input('Первое число: '))
b = int(input('Второе число: '))

def nok(a, b):
   noc = (a * b) / gcd(a, b)
   return noc

def gcd(a, b):
   "Нахождение НОД: пример взят из доклада-презентации Гвидо ван Россума"
   while a != 0:
      a,b = b%a,a # параллельное определение
   return b

print ("НОК:", nok(a, b))
