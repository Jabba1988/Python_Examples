from tkinter import *
from time import *

окно = Tk()                 # Вывод окна
окно.title(" Начало ")      # заголовок окна
окно.geometry('500x250')    # размер окна

холст = Canvas(окно, bg='white', width=480, height=240) # задать холст для рисования
холст.pack() # вывести холст

холст.create_oval(30,10,130,110,fill="orange") # нарисовали на холсте овал
холст.create_rectangle(180,60,280,160,tag="rect",fill="lightgreen")
холст.create_text(220,20,fill="VioletRed", font="arial",text="Вот попробуйте..." )
