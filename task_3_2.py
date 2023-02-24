'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
'''
input_number = int(input('Введите длину исследуемого массива:  '))
inv_array = list()
for i in range(input_number):
    inv_array.append(int(input(f'Введите {i+1} элемент исследуемого массива: ')))
print(f'Сформированный массив выглядит следующим образом: {inv_array}')
input_number = int(input('Введите некоторое число Х:  '))
diff_number = inv_array[0]
for i in inv_array:
    if abs(i - input_number) < abs(diff_number - input_number):
        diff_number = i
print(f'Самый близкий по величине элемент к заданному числу Х={input_number} в исследуемом масиве равен {diff_number}')