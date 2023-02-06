# Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
# Размер списка n ввести с клавиатуры. Найти значение максимального элемента списка.

import random

n = int(input("Enter the size of the list:\n"))
array = [random.randint(0, 99) for i in range(n)]

print("The list is:", array)

max_val = array[0]
for i in range(1, n):
    if array[i] > max_val:
        max_val = array[i]

print("The maximum value in the list is:", max_val)
