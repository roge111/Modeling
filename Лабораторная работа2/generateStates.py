def generateStates(en): 
    en = list(map(int, en.split('/')))
    print('Начинаю генерацию состояний .', end=' ')
    E = []
    if len(en) == 2:
        for x in range(en[0]+2):
            if x == en[0]+1:
                print('.')
            else:
                print('.', end=' ')
            for y in range(en[1]+2):
                E.append([x, y])
    elif len(en) == 3:
        for x in range(en[0]+2):
            if x == en[0]:
                print('.')
            else:
                print('.', end=' ')
            for y in range(en[1]+2):
                for z in range(en[2] + 2):
                    E.append([x, y, z])
    print('Генерация состояний завершена. Ниже список состояний:')
    return E

print(generateStates('3/0'))