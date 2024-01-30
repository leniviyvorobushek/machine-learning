n = int(input('Введите количство строк: '))
text = [input() for i in range(n)]

for j in text:
    if j[:4] == '####':
        continue
    if j[:2] == '%%':
        print(j[2:])
    else:
        print(j)