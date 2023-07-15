import unittest

from lab05.Tribonacci import Tribonacci


class TribonacciTests(unittest.TestCase):
    def setUp(self):
        self.tribonacci_sequence = Tribonacci()

    def test_sequence_generation(self):
        expected_sequence = [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513,
                             35890, 66012, 121415, 223317, 410744, 755476, 1389537, 2555757, 4700770, 8646064, 15902591,
                             29249425, 53798080, 98950096]

        generated_sequence = [next(self.tribonacci_sequence) for _ in range(len(expected_sequence))]

        self.assertEqual(generated_sequence, expected_sequence)

    def test_stop_iteration(self):
        # Generate more terms than the defined limit of 35
        with self.assertRaises(StopIteration):
            for _ in range(36):
                next(self.tribonacci_sequence)

if __name__ == '__main__':
    unittest.main()
