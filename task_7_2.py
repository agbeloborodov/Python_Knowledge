'''Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент
по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов
идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
*Пример:*
**Ввод:** `print_operation_table(lambda x, y: x * y) `
**Вывод:**
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
'''
def print_operation_table(operation, num_rows, num_сolumns):
    arr=[[operation(i,j) for i in range(1,num_rows+1)] for j in range(1, num_сolumns+1)]
    for i in arr:
        print(*[f"{x:5}"for x in i])
rows = int(input("Введите количество строк таблицы: "))
columns = int(input("Введите количество столбцов таблицы: "))
print('Есть некоторый выбор бинарных операций:')
print('1. x+y\n2. x-y\n3. x*y\n4. x/y\n5. x**y')
choose = int(input('Введите вариант вычисления элементов матрицы (1, 2, 3, 4 или 5):  '))
if choose == 1: print_operation_table(lambda x,y: x + y, rows, columns)    # У меня python 3.6.9, поэтому конструкция match/case не получилась
elif choose == 2: print_operation_table(lambda x,y: x - y, rows, columns)
elif choose == 3: print_operation_table(lambda x,y: x * y, rows, columns)
elif choose == 4: print_operation_table(lambda x,y: round((x / y), 2), rows, columns)
elif choose == 5: print_operation_table(lambda x,y: x ** y, rows, columns)
else: print('Определитесь уже, что Вам угодно. Всего хорошего!')