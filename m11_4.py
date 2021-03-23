letters = 'абвгдеёжзийклмнопрстуфхцчшщъыэюя'
stings_for_search = input("Введите строку для разбора ")
dictionary = {letter: 0 for letter in letters}
for i in stings_for_search:
     if i in dictionary:
          dictionary[i] += 1
print (dictionary.items())
