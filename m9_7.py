from random import *

listofsportsmens = ["Ivanov", "Petrov", "Zaycev"]


def randresult(b):
    a = []
    for i in range(len(b)):
        a.append(randint(2, 5))
    return a    
    

def splitter(a):
    b = []
    c = []
    for i in a:
        if a[i] < 0 :
            c.append(a[i])
        else:
            b.append(a[i])
    print (b, "\n", c)

print(randresult(listofsportsmens))


#//TODO

