# Про смесь
n = 1
i = 0
раствор = []
# ввод весов
while n!=0:
  n = float(input('Вес компоненты раствора (0 - завершение ввода) - '))
  if n > 0:
      раствор = раствор + [n]
print('Структура раствора: ', раствор)
# определение процентного содержания
проценты = раствор
a = sum(проценты)    # определили сумму элементов списка
for i in range(len(проценты)):
    проценты[i] = проценты[i]*100/a
    print(i)
    
print('Проценты - ', проценты)

