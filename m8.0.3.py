from tkinter import *
root = Tk()
c = Canvas(width=200, height=200, bg='white')
c.pack()

c.create_oval(30,10,130,80,tag="group1")     # эллипс и линия содержат один
c.create_line(10,100,450,100,tag="group1")   # и тот же тег groupl
 
def color(event):
     c.itemconfig('group1',fill="red",width=3)

c.bind('<Button-3>',color)         # Так обрабатывается событие "Нажатие
                                   # правой клавиши мыши". Button-1 - левой...
root.mainloop()
