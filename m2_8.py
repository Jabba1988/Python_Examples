from tkinter import *

окно = Tk()                 # Вывод окна
окно.title(" Начало ")      # заголовок окна
окно.geometry('800x600')    # размер окна

холст = Canvas(окно, bg='white', width=800, height=600) # задать холст для рисования
холст.pack() # вывести холст

# Примеры
холст.create_arc([160,230],[230,330],start=0,extent=140,fill="lightgreen")
холст.create_arc([250,230],[320,330],start=0,extent=140, style=CHORD,fill="green")
холст.create_arc([340,230],[410,330],start=0,extent=140,style=ARC,outline="darkgreen",width=2)
# Части окружности
холст.create_oval(10, 10, 190, 190, fill='lightgrey', outline='white')
холст.create_arc(10, 10, 190, 190, start=0, extent=45, fill='red')
холст.create_arc(10, 10, 190, 190, start=180, extent=25, fill='orange')
холст.create_arc(10, 10, 190, 190, start=240, extent=100, style=CHORD, fill='green')
холст.create_arc(10, 10, 190, 190, start=160, extent=-70, style=ARC, outline='darkblue', width=5)
