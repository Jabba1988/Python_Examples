from tkinter import *
окно = Tk()
окно.geometry('800x600+50+50')  # 50 - смещение по оси х и у

холст = Canvas(окно, width=800, height=600)

photo =PhotoImage(file='fruit.png')      # создание изображения в памяти

а = холст.create_image(1,1,anchor=NW,image=photo) # вывод картинки на холст

холст.place(x=10,y=100)         # размещение картики относительно начала координат

def motion():                    # функция движения объекта
    холст.move(а, 1, 0)          # метод move изменяет координату х объекта на 1
    if холст.coords(а)[1] < 300: # определяется вторая координаты объекта ballв
        окно.after(10, motion)
   
motion()

окно.mainloop()
