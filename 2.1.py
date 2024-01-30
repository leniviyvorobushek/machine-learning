n = int(input('Введите количство чисел: '))
l = [int(input()) for i in range(n)]

l = sorted(l)
l.reverse()
print(l)