n = int(input('Введите количество чисел: '))
l = [int(input()) for i in range(n)]

p = int(input('Введите начальный номер элемента списка, который нужно просуммировать: '))
q = int(input('Введите конечный номер элемента списка, который нужно просуммировать: '))

counter = 0
summa = 0
for i in l:
    counter += 1
    if (counter >= p) and (counter <= q):
        summa += i
print(summa)
