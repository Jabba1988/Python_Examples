from tkinter import *
 
root = Tk()
c = Canvas(root, width=300, height=200, bg="blue")
c.pack()
 
ball = c.create_oval(0, 100, 40, 140, fill='yellow')
 
def motion():
    c.move(ball, 1, 0)          # метод move изменяет координату х объекта на 1
    if c.coords(ball)[2] < 300: # определяется вторая координаты объекта ball
        root.after(10, motion)

# Метод after() вызывает функцию, переданную вторым аргументом,
# через количество миллисекунд, указанных первым аргументом.
# В данном случае - саму себя (рекурсия)
 
motion()
 
root.mainloop()
