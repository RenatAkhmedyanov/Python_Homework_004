# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12

import random

n = int(input('Введите количество элементов первого набора: '))
m = int(input('Введите количество элементов второго набора: '))

def create_list(x):
    list = []
    for i in range(x):
        random_number = random.randint(0, 10)
        list.append(random_number)
    return list

list_1 = create_list(n)  
list_2 = create_list(m)
print(list_1)
print(list_2)

set_1 = set(list_1)
set_2 = set(list_2)
result = list(set_1.intersection(set_2))
result.sort()
print(f'Значения, которые встречаются в обоих наборах: {result}')