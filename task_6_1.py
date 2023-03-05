''' Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки. '''

first_member = int(input('Введите первый элемент арифметической прогрессии: '))
progr_lenght = int(input('Введите количество элементов арифметической прогрессии: '))
step_progr = int(input('Введите шаг арифметической прогрессии: '))
list_progression = []
list_progression.append(first_member)
for i in range(1, progr_lenght):
    list_progression.append(first_member + i * step_progr)
print(f'Получившаяся арифметическая прогрессия:  {list_progression}')