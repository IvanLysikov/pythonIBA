import datetime


class Car:
    __id = 0

    def __init__(self, brand, model, year, color, price, reg_number):
        self.__brand = brand
        self.__model = model
        self.year = year
        self.color = color
        self.price = price
        self.reg_number = reg_number
        Car.__id += 1
        self.__id = Car.__id

    def get_id(self):
        return self.__id

    def get_brand(self):
        return self.__brand

    def set_brand(self, new_brand):
        if isinstance(new_brand, str):
            self.__brand = new_brand
        else:
            raise ValueError("Brand should be a string")

    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        if isinstance(new_model, str):
            self.__model = new_model
        else:
            raise ValueError("Model should be a string")

    @staticmethod
    def get_car_age(car):
        current_year = datetime.datetime.now().year  # текущий год
        return current_year - car.year

    @classmethod
    def get_id(cls):
        return cls.__id

    def __str__(self):
        return f"{self.__id} {self.__brand} {self.__model} ({self.year}), {self.color}, {self.price}, {self.reg_number}"

    def __repr__(self):
        """Возвращает строковое представление объекта для его воссоздания."""
        return f"Car({self.__brand}, {self.__model}, {self.year})"

    def __eq__(self, other):
        """Определяет поведение оператора равенства (==)."""
        if isinstance(other, Car):
            return (
                    self.get_brand() == other.get_brand() and
                    self.get_model() == other.get_model() and
                    self.year == other.year and
                    self.color == other.color and
                    self.price == other.price and
                    self.reg_number == other.reg_number
            )
        return False

    def __gt__(self, other):
        """Определяет поведение оператора больше (>), сравнивая годы выпуска."""
        if isinstance(other, Car):
            return self.year > other.year
        return False

    def __lt__(self, other):
        """Определяет поведение оператора меньше (<), сравнивая годы выпуска."""
        if isinstance(other, Car):
            return self.year < other.year
        return False

    def __add__(self, other):
        """Определяет поведение оператора сложения (+) для объединения двух автомобилей."""
        if isinstance(other, Car):
            # Создаем новый автомобиль с объединенными данными
            brand = f"{self.__brand} {other.__brand}"
            model = f"{self.__model} {other.__model}"
            year = max(self.year, other.year)
            color = f"{self.color} {other.color}"
            price = self.price + other.price
            reg_number = f"{self.reg_number} {other.reg_number}"
            return Car(brand, model, year, color, price, reg_number)
        else:
            raise TypeError("Unsupported operand type for +")

