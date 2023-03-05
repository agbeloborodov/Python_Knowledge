''' Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)'''

from random import randint

investig_list = [randint(-21, 21) for _ in range(21)]
print(f'Случайным образом сгенерирован следующий массив:  {investig_list}')
min_number = int(input('Введите минимальное число: '))
max_number = int(input('Введите максимальное число: '))
index_list = list()
for i in range(len(investig_list)):
    if min_number <= investig_list[i] <= max_number:
        index_list.append(i)
print(f'Индексы элементов массива, входящие в указанный диапазон:  {index_list}')