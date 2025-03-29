import pandas as pd
import generateStates as gs
# num = int(input("Введите порядкой номер в группе>> "))
# var_last = str(num + 32)

# print(f"Ваша система 1 = {var_last[0]}")
# print(f'Ваша система 2 = {var_last[1]}')
# print(f'Ваша система 3 = {num}')

countDevices = int(input("Введи количество приборов>> "))

P = list(map(float, input("Введи через пробел вероятности занимая приборов 1, 2 и 3>> ").split()))

if countDevices == 1:
    P = 1
elif countDevices == 2:
    P1 = P[0]
    P2 = P[1] + P[2]
else:
    P1 = P[0]
    P2 = P[1]
    P3 = P[2]

l = float(input("Введите интенсивность потока>> "))

# en = input('Для начала работы введите X/Y/Z из варианта -> ')
# en = list(map(int, en.split('/')))

# states = gs.generateStates(en)
#Выше был код, который по ЕН генерирует состояния. Графы пока рисуються в ручную

#После рисования графы вход пишется номер точки графы и графы, с которымы эта тока связана. например, 0:1,2;2:3,4

print("Введите данные графа в виде: номер вершины 1: вершина 2, вершина 3/и тд")
data = input().split('/')

hash_map = {}
max_len = 0
array_key = {}
for point in data:
    point = point.split(':')
    
    hash_map[point[0]] = point[1].split(',')
    
    

    max_len = max(len(hash_map[point[0]]), max_len)

sort_keys = sorted(hash_map)
print(hash_map)
result = {}
if countDevices == 2:
    for point in sort_keys:
        cue = hash_map[point]
        if len(cue) == max_len:
            result[point] = [round(l*P1, 4), round(l*P2, 4)]
        elif len(cue) == 1 and int(point) == len(hash_map)-1:
            result[point] = [round(l*P2, 4)]
        else:
            result[point] = [round(l*P1, 4)]
print(result)

