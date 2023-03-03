'''Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''

def other_exp(base, rank):
    if rank == 0:
        return 1
    elif rank < 0:
        return round(((1 / base) * other_exp(base, rank + 1)), abs(rank))
    else:
        return base * other_exp(base, rank - 1)

input_a = int(input('Введите число A (основание степени):  '))
input_b = int(input('Введите число B (показатель степени):  '))
print(f'Результат выражения {input_a}**({input_b}) равен {other_exp(input_a, input_b)}')