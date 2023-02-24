'''Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста
есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте
выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения
максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
'''

input_bb = int(input('Введите количество кустов черники:  '))
bb_array = list()
for i in range(input_bb):
    bb_array.append(int(input(f'Введите количество ягод на {i+1} кусту черники:  ')))
print(f'Количество ягод на каждом из кустов: {bb_array}')
inv_array = list()
for i in range(len(bb_array)-1):
    inv_array.append(bb_array[i-1] + bb_array[i] + bb_array[i+1])
print(f'Комбинации единовременного сбора ягод:  {inv_array}')
print(f'Ответ: {max(inv_array)} ягод')