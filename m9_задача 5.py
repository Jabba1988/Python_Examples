from random import *

def listOf():
    a = []
    for i in range(1,31):
        a.append(randint(2, 5))
    return a    
    
def mean(a):
    print(a)
    col_5 = []
    col_4 = []
    col_3 = []
    col_2 = []
    j = 0
    for i in range(len(a)):
        if a[j] == 5:
            col_5.append(a[j])
            j += 1
        elif a[j] == 4: 
            col_4.append(a[j])
            j += 1
        elif a[j] == 3:
            col_3.append(a[j])
            j += 1
        else:
            col_2.append(a[j])
            j += 1
    
    print("5:", len(col_5), "4: ", len(col_4), "3: ", len(col_3), "2: ", len(col_2))

mean(listOf())
