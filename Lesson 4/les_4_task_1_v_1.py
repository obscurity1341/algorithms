#Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
#Примечание. Идеальным решением будет:
#● выбрать хорошую задачу, которую имеет смысл оценивать,
#● написать 3 варианта кода (один у вас уже есть),
#● проанализировать 3 варианта и выбрать оптимальный,
#● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
#● написать общий вывод: какой из трёх вариантов лучше и почему.


# 4-я задача 3-го урока.
import random
import timeit
import cProfile

#MIN_ITEM = 0
#print(array)

# вариант 1
def max_count(size):
    num = array[0]
    amount_max = 1
    for i in range(size-1):
        amount = 1
        for j in range(i + 1, size):
            if array[i] == array[j]:
                amount += 1
            if amount > amount_max:
                amount_max = amount
                num = array[i]
    return f'Число {num} встречается {amount_max} раз'
size = 1000
array = [random.randint(size*0, size) for _ in range(size)]

s = '''
def max_count(size):
    num = array[0]
    amount_max = 1
    for i in range(size-1):
        amount = 1
        for j in range(i + 1, size):
            if array[i] == array[j]:
                amount += 1
            if amount > amount_max:
                amount_max = amount
                num = array[i]
    return f'Число {num} встречается {amount_max} раз'
size = 1000
array = [random.randint(size*0, size) for _ in range(size)]
'''

#print(timeit.timeit(s, number=10000, globals=globals()))
#17.3502793


cProfile.run('max_count(1, 10000)')

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.007    0.007    0.007    0.007 <string>:1(<module>)
#       1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

