# Даны две квадратных таблицы чисел.
# Требуется построить третью, каждый элемент которой равен сумме элементов,
# стоящих на том же месте в 1-й и 2-й таблицах.
import random


def generate_array(length):
    return [random.randint(-100, 100) for i in range(length)]


def pretty_print(value, max_number_length=4):
    value_length = len(str(value))
    diff = max_number_length - value_length
    spaces = " " * (diff + 1)
    print(f"{spaces}{value}", end="")


def pretty_matrix_print(array, _definition):
    max_number_length = calculate_max_number_length(array) if _definition is None else _definition
    for i in range(len(array)):
        for j in range(len(array[i])):
            pretty_print(array[i][j], max_number_length)
        print()


def calculate_max_number_length(lst):
    flatten_lst = flatten(lst)
    max_value = max(flatten_lst)
    min_value = min(flatten_lst)
    min_value_length = len(str(min_value))
    max_value_length = len(str(max_value))
    return min_value_length if min_value_length >= max_value_length else max_value_length


def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def sum_of_matrix(matrix1, matrix2):
    sum_of_matrix = []
    for i in range(len(matrix1)):
        sum_of_matrix.append([])
        for j in range(len(matrix1[i])):
            sum_of_matrix[i].append(matrix1[i][j]+matrix2[i][j])
    return sum_of_matrix


list_length = 10

# generating two matrix:
matrix1 = [generate_array(list_length) for i in range(list_length)]
matrix2 = [generate_array(list_length) for i in range(list_length)]

# printing
pretty_matrix_print(matrix1, 5)
print()
pretty_matrix_print(matrix2, 5)
print()

# calculating
sum_of_matrix = sum_of_matrix(matrix1, matrix2)

# printing
pretty_matrix_print(sum_of_matrix, 5)
