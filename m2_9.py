from tkinter import *

окно = Tk()                 # Вывод окна
окно.title(" Начало ")      # заголовок окна
окно.geometry('400x200')    # размер окна

холст = Canvas(окно, bg='white', width=400, height=200) # задать холст для рисования
холст.pack() # вывести холст

# линия

холст.create_text(200,95,text="Текст в canvas",font="Verdana 24",justify=CENTER,fill="red")

