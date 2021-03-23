# Функция. Преобразуем текстовый файл в словарь
def file_dict(name1):
    f1 = open(name1)                  # открыли файл для чтения
    строка = f1.read()                # считали ВЕСЬ файл в строку а
    список = строка.split()           # преобразовали строку в список
    словарь = {}
    i=0
    while i<len(список):              # преобразовали список в словарь    
       словарь[список[i]]=список[i+1]
       i+=2
    return словарь

##___________________________________________________
def dict_file(name2,словарь):
    # Функция. Преобразуем словарь в текст и записываем в файл на диске
    f2 = open(name2, 'w')                      # открыли файл для чтения
    for ключ in словарь:
         f2.write(ключ+' '+словарь[ключ]+'\n') # записали в файл строку	
    f2.close()
#____________________________________________________
d = file_dict('Телефоны.txt')  # в словарь записали данные из текстового файла
for key,value in d.items():
        print(key,value)       # так можно выводить словарь
dict_file('Телефоны2.txt',d)   # сохранили словарь в виде текстового файла 




	