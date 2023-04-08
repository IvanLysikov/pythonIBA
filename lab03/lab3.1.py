import random
import datetime
import prettytable               # пакет для таблицы
import matplotlib.pyplot as plt  # библиотека для графика


def BubbleSort(A):  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a


def QuickSort(A, fst, lst):  # быстрая сортировка
    if fst >= lst:
        return

    # i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst + 1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger + 1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger - 1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller - 1)
    QuickSort(A, first_bigger, lst)


def MergeSort(arr):  # сортировка слиянием
    # Проверяем, что длина массива больше 1
    if len(arr) > 1:
        # Находим середину массива
        mid = len(arr) // 2
        # Делим массив на две половины
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Рекурсивно вызываем функцию сортировки для левой половины
        MergeSort(left_half)
        # Рекурсивно вызываем функцию сортировки для правой половины
        MergeSort(right_half)

        # Создаем переменные-счетчики
        i = j = k = 0

        # Объединяем отсортированные левую и правую половины
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Объединяем оставшиеся элементы левой половины
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Объединяем оставшиеся элементы правой половины
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    # Возвращаем отсортированный массив
    return arr


table = prettytable.PrettyTable(["Размер списка", "Merge", "Quick", "Bubble"])
x = []
y1 = []
y2 = []
y3 = []

for N in range(100, 501, 20):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))


    B = A.copy()
    C = A.copy()

    t1 = datetime.datetime.now()
    MergeSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("Сортировка слиянием   " + str(N) + "   заняла   " + str((t2 - t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B) - 1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая сортировка  " + str(N) + "   заняла   " + str((t4 - t3).total_seconds()) + "c")

    t5 = datetime.datetime.now()
    BubbleSort(C)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    print("Пузырьковая сортировка  " + str(N) + "   заняла   " + str((t6 - t5).total_seconds()) + "c")

    table.add_row(
        [str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds()), str((t6 - t5).total_seconds())])
print(table)

plt.plot(x, y1, label='Merge Sort')
plt.plot(x, y2, label='Quick Sort')
plt.plot(x, y3, label='Bubble Sort')
plt.xlabel('Size of Array')
plt.ylabel('Execution Time (s)')
plt.title('Sorting Algorithms Comparison')
plt.legend()
plt.show()
