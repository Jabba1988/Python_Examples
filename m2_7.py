from tkinter import *

окно = Tk()                 # Вывод окна
окно.title(" Начало ")      # заголовок окна
окно.geometry('500x250')    # размер окна

холст = Canvas(окно, bg='white', width=480, height=240) # задать холст для рисования
холст.pack() # вывести холст

# произвольный многоугольник: сколько пар координат добавите, столько вершин и будет
холст.create_polygon(30,80,360,10,430,80,fill='red',outline="black",smooth=0)
