# Найдите наибольший элемент списка, затем удалите его и выведите новый список.
import random

list_length = 10
random_numbers = [random.randint(-100, 100) for i in range(list_length)]

print(f"random generated list: {random_numbers}")
max_value = max(random_numbers)
print(f"maximum value is: {max_value}")
random_numbers.remove(max_value)
print(f"previous list without maximum value: {random_numbers}")
