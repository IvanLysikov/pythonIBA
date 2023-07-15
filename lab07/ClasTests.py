import unittest
from datetime import datetime

from lab05.Car import Car


class CarTest(unittest.TestCase):
    def setUp(self):
        self.car1 = Car("Toyota", "Camry", 2015, "Red", 15000, "ABC123")
        self.car2 = Car("Honda", "Accord", 2018, "Blue", 20000, "XYZ789")

    def test_get_brand(self):
        self.assertEqual(self.car1.get_brand(), "Toyota")
        self.assertEqual(self.car2.get_brand(), "Honda")

    def test_set_brand(self):
        self.car1.set_brand("Lexus")
        self.assertEqual(self.car1.get_brand(), "Lexus")

        with self.assertRaises(ValueError):
            self.car2.set_brand(123)

    def test_get_model(self):
        self.assertEqual(self.car1.get_model(), "Camry")
        self.assertEqual(self.car2.get_model(), "Accord")

    def test_set_model(self):
        self.car1.set_model("Corolla")
        self.assertEqual(self.car1.get_model(), "Corolla")

        with self.assertRaises(ValueError):
            self.car2.set_model(123)

    def test_get_car_age(self):
        current_year = datetime.now().year
        self.assertEqual(Car.get_car_age(self.car1), current_year - self.car1.year)

    def test_eq(self):
        car3 = Car("Toyota", "Camry", 2015, "Red", 15000, self.car1.reg_number)
        self.assertTrue(self.car1 == self.car1)
        self.assertTrue(self.car1 == car3)

    def test_gt(self):
        self.assertTrue(self.car2 > self.car1)
        self.assertFalse(self.car1 > self.car2)

    def test_lt(self):
        self.assertTrue(self.car1 < self.car2)
        self.assertFalse(self.car2 < self.car1)

    def test_add(self):
        car3 = Car("Toyota", "Corolla", 2020, "Silver", 20000, "GHI789")
        combined_car = self.car1 + car3
        self.assertEqual(combined_car.get_brand(), "Toyota Toyota")
        self.assertEqual(combined_car.get_model(), "Camry Corolla")
        self.assertEqual(combined_car.year, max(self.car1.year, car3.year))
        self.assertEqual(combined_car.color, "Red Silver")
        self.assertEqual(combined_car.price, self.car1.price + car3.price)
        self.assertEqual(combined_car.reg_number, "ABC123 GHI789")

    def test_add_invalid_operand(self):
        with self.assertRaises(TypeError):
            self.car1 + 123

if __name__ == "__main__":
    unittest.main()
