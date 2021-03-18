from random import *

def listOfprecipitation():
    a = []
    for i in range(1,32):
        a.append(randint(0, 100))
    return a    
    
def mean(a):
    col = 0
    for i in range(len(a)):
        col += a[i]    
    print("mean: ", col, " mm")

mean(listOfprecipitation())
