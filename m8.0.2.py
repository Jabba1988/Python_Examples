from tkinter import *
root = Tk()
c = Canvas(width=200, height=200, bg='white')
c.pack()
 
rect = c.create_rectangle(80, 80, 120, 120, fill='lightgreen')
 
def inFocus(event):
    c.itemconfig(rect, fill='red', width=2) # изменяются свойства rect
    c.coords(rect, 70, 70, 130, 130)        # изменяются координаты
#-----------------------------------------------------------------
c.bind('<FocusIn>', inFocus)    #Метод bind реагирует на Tab
                                # и вызывает функцию inFocus
 
root.mainloop()
