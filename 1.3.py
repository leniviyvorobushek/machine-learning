while True:
    slova = input()
    minx = slova
    maxx = slova
    if slova == 'стоп':
        if len(set(minx) - set(maxx)) == 0:
            print('ДА')
            break
        else:
            print('НЕТ')
            break
    if len(slova) > len(maxx):
        maxx = slova
    if len(slova) < len(minx):
        minx = slova