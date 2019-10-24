#Определить, какое число в массиве встречается чаще всего.

import random

SIZE = int(input('Введите величину массива:'))
MIN_ITEM = 2
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


num = array[0]
nums = []
amount_max = 1
for i in range(SIZE-1):
    amount = 1
    for j in range(i+1, SIZE):
        if array[i] == array[j]:
            amount += 1
        if amount > amount_max:
            amount_max = amount
            num = array[j]
            if amount_max > 1:
                nums.append(num)
print(amount_max, ' - ', num)
print(nums)
