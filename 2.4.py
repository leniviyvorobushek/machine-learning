def Artek(s, n):
    s = s.split(', ')
    artek = []
    for i in s:
        if i[-1] == '5':
            artek.append(i[:-2])
    artek = sorted(artek)
    if len(artek) > n:
        return (", ".join(artek[0:n]))
    else:
        return (", ".join(artek))


s = str(input('Введите учеников и их оценки: '))
n = int(input('Введите количество свободных мест: '))
print(Artek(s, n))