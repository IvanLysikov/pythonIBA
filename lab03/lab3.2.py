def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def num_squares(a, b, squares):
    a //= squares
    b //= squares
    return a * b


a = int(input("Введите длину прямоугольника: "))
b = int(input("Введите ширину прямоугольника: "))
square_side = gcd(a, b)
num_squares = num_squares(a, b, square_side)
print("Длины ребер полученных квадратов:", square_side)
print("Количество полученных квадратов:", num_squares)
