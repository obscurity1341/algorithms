# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

import random

array = range(2, 9)

sum_column = [0] * len(array)
for i in range(2, 99):
    for j in range(2, 9):
        if i % j == 0:
            sum_column[j - 2] += 1
i = 0
while i < len(sum_column):
    print(i + 2, 'кратно', sum_column[i])
    i += 1
