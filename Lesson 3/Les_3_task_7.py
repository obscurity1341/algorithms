# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

SIZE = int(input('Введите величину массива:'))
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


if array[0] < array[1]:
    min_1 = 0
    min_2 = 1
else:
    min_1 = 1
    min_2 = 0


for i in range(2, SIZE-1):
    if array[i] < array[min_1]:
        new_i = min_1
        min_1 = i
        if array[new_i] < array[min_2]:
            min_2 = new_i
    elif array[i] < array[min_2]:
        min_2 = i
print(array[min_1], array[min_2])

