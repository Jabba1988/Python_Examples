# Задача. Составить программу, которая должна  вычислять  частоту использование
#         русских букв в введенном тексте.
#   Задание.  
#        Вам дана уже готовая часть программы, обеспечивающая ввод произвольного
#        текста и  вычисление  количества каждой буквы в введенном тексте. Измените
#        и допишите программу так, чтобы она выдавала на экран процентное содержание
#        каждой из букв, имеющейся в тексте.

буквы = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# Создали пустой список из 0-ых элементов длиной строки буквы
частоты = [0 for i in range(len(буквы))]
print(частоты) # посмотрели, как это выглядит

s = input('Введите текст: ')
s = s.lower()
# привели данные к нижнему регистру
# посчитали частоту:
for c in s:
    if c in буквы:
        частоты[буквы.find(c)] +=1
        
# вывели результат:
for i in range(len(частоты)):
    print('%s - %7d' % (буквы[i], частоты[i]))


