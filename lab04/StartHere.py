from lab04.Car import Car

# создание списка объектов

cars = [
    Car("Toyota", "Camry", 2010, "черный", 5000, "AB1234"),
    Car("Honda", "Accord", 2017, "серый", 9000, "CD3456"),
    Car("BMW", "X5", 2018, "белый", 15000, "DE4567"),
    Car("Toyota", "Corolla", 2015, "синий", 7000, "BC2345"),
    Car("BMW", "X5", 2010, "серебристый", 8000, "EF5678"),
    Car("Mercedes-Benz", "E-Class", 2016, "черный", 12000, "FG6789")
]

# вывод списка автомобилей заданной марки
toyota_cars = [car for car in cars if car.get_brand() == "Toyota"]
print("Список автомобилей марки Toyota:")
for car in toyota_cars:
    print(car)

# вывод списка автомобилей заданной модели, которые эксплуатируются больше n лет
n = 5  # количество лет
x5_cars = [car for car in cars if car.get_model() == "X5" and Car.get_car_age(car) > n]
print(f"\nСписок автомобилей модели BMW X5, которые эксплуатируются больше {n} лет:")
for car in x5_cars:
    print(car)
