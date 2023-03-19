# Найдите сумму номеров минимального и максимального элементов.
import random

list_length = 10
random_numbers = [random.randint(-100, 100) for i in range(list_length)]

max_value = max(random_numbers)
min_value = min(random_numbers)
max_value_index = random_numbers.index(max_value)
min_value_index = random_numbers.index(min_value)

print(f"random generated list: {random_numbers}")
print(f"maximum value is: {max_value} with index: {max_value_index}")
print(f"minimum value is: {min_value} with index: {min_value_index}")
print(f"sum of indexes is: {min_value_index + max_value_index}")
