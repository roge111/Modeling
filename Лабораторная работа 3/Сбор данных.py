import pandas as pd
count = 4 #Количество испытаний
#Пордок значений такой: процент потерь, длина очереди, загрузка, среднее время ожидания
data = {}
for i in range(count):
    in_data  = list(map(float, input().split()))
    data[f'Вариант {i + 1}'] = in_data

df = pd.DataFrame(data)
name_file = input('Введите имя файла без .csv')
df.to_csv(name_file + '.csv', encoding='utf-8')
