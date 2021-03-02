from tkinter import *
 
c = Canvas(width=460, height=100, bg='grey80')
c.pack()
 
# этот объект определяется идентификатором
oval = c.create_oval(30, 10, 130, 80, fill="orange")
# этот объект - тегом
c.create_rectangle(180, 10, 280, 80,tag="rect", fill="lightgreen")
# этот объект снова идентификатором
trian = c.create_polygon(330, 80, 380, 10, 430, 80,fill='white',outline="black")
 
def oval_func(event):    # событие event имеет здесь важно. Например, event.x
                         # event.y - координаты объекта
                         
     c.delete(oval)      # delete - метод, удаляющий объект с холста
     c.create_text(80, 50, text="Круг")
     
def rect_func(event):
     c.delete("rect")
     c.create_text(230, 50, text="Прямоугольник")
     
def triangle(event):
     c.delete(trian)
     c.create_text(380, 50, text="Треугольник")
 
c.tag_bind(oval, '<Button-1>', oval_func)    # если щелкнуть ЛКМ по oval
c.tag_bind("rect", '<Button-1>', rect_func)  # если щелкнуть ЛКМ по rect 
c.tag_bind(trian, '<Button-1>', triangle)    # если щелкнуть ЛКМ по trian 
 
mainloop() 
