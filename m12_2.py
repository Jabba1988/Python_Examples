f = open('numbers.txt', 'r')
line = f.readline()
b = 0
count = 0
for i in line:
    b += float(i)
    count += 1
print("Среднее арифметическое: ", b/count)
f.close()
