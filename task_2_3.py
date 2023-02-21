'''Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''

input_number = int(input('Введите число N: '))
temp_value = 0
while 2 ** temp_value <= input_number:
    print(f'{2 ** temp_value}', end = '  ')
    temp_value += 1