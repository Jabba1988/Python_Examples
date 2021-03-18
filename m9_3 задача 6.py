# Про смесь
n = 1
i = 0
l = ""
listofIngredients = []
раствор = []
# ввод весов
while n!=0 :
  l = str(input('Name of component (0 - stop entering) '))
  n = float(input('Вес компоненты раствора (0 - завершение ввода) - '))
  if n > 0:
      раствор.append(n)
      listofIngredients.append(l)
print('Структура раствора: ', раствор, listofIngredients)
# определение процентного содержания
проценты = раствор
a = sum(проценты)    # определили сумму элементов списка
for i in range(len(проценты)):
    проценты[i] = проценты[i]*100/a
    print('Проценты - ', проценты[i], listofIngredients[i])

