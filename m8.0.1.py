from tkinter import *
root = Tk()
c = Canvas(width=300, height=300, bg='white')
c.focus_set()   #передать фокус виджету - чтобы обрабатывались нажатия кнопок
c.pack()
 
ball = c.create_oval(140, 140, 160, 160, fill='lightblue')

c.bind('<Up>', lambda event: c.move(ball, 0, -2))       # Клавиша вверх
c.bind('<Down>', lambda event: c.move(ball, 0, 2))      # Клавиша вниз
c.bind('<Left>', lambda event: c.move(ball, -2, 0))     # Клавиша влево 
c.bind('<Right>', lambda event: c.move(ball, 2, 0))     # Клавиша вправо 
 
root.mainloop()
