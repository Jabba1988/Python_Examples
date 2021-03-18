m = []
b = []
col = 0
a = int(input('Кол-во спортсменов: '))
for i in range(a):
    print("Оценка спортсмена ", i + 1)
    m = m + [int(input('Число = '))]
srball = sum(m)/a
for i in m:
    if i > srball:
        b.append(i)
    else:
        pass

print("Прошли на соревнавания", len(b))