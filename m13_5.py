from tkinter import *
root=Tk()
button1 = Button(text="Левая", bg = 'Red')
button2 = Button(text="Верх", bg = 'orange')
button3 = Button(text="Низ",bg = 'Yellow')
button4 = Button(text="Право", bg = 'Green')
button1.pack(side='left')
button2.pack(side='top')
button3.pack(side='bottom')
button4.pack(side='right')
root.mainloop()
