a = input("Введите название файла")
f = open(a, 'w')
text = input("Что пишем в файл? Чтобы выйти введите exit")
if text == "exit": 
   f.close()
   exit()
else:
   f.write(text)
   f.close