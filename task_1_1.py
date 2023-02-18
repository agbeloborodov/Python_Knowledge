'''Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
'''

input_number = int(input('Введите трёхзначное число: '))
temp_value = 0
if 99 < input_number < 1000:
    while input_number != 0:
        temp_value += input_number % 10
        input_number //= 10
    print(f'Сумма цифр введённого Вами трёхзначного числа равна {temp_value}')
else:
    print('Вы ввели не трёхзначное число')