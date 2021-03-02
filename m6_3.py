from tkinter import *
from random import *

windows = Tk()                 # Вывод окна
windows.title(" ММденс ")      # заголовок окна
windows.geometry('640x480')    # размер окна

win = Canvas(windows, bg='white', width=640, height=480) # задать холст для рисования
win.pack() # вывести win

col = ["lavender", "SlateBlue","green","yellow","chocolate","DeepPink","BlueViolet",
       "purple2","red1","coral1","wheat1","gold1","SpringGreen1","orange"]

for i in range(5000):
    x = randint(-20,640); y = randint(-20,480)
    a = randint(10,60); b = randint(10,60)
    c = randint(0,13)
    win.create_rectangle(x, y, x+a, y+b, fill=col[c])


windows.mainloop()