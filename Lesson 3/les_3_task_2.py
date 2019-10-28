#Во втором массиве сохранить индексы четных элементов первого массива.
#Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
#т.к. именно в этих позициях первого массива стоят четные числа

import random

SIZE = int(input('Введите длину массива:'))
MIN_ITEM = 1
MAX_ITEM = 100
massive_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(massive_1)

massive_2 = []
for i in range(len(massive_1)):
    if massive_1[i] % 2 == 0:
        massive_2.append(i)
print(i)
print(massive_2)