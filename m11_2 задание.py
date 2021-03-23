surnames = {}
print("Для выхода напишите exit")
phone_number = input('Ищем номер: ')

while True:
    if phone_number in surnames:
        print("Есть запись: ", surnames[phone_number])
    elif phone_number == "exit" :
        print(surnames)
        False
    else:
        surname = input('Введите фамилию')
        surnames[phone_number] = surname
        print("Добавили ", surname, surnames[phone_number])
