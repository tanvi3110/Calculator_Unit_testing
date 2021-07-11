import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data1 = CsvReader('tests/Data/subtraction.csv').data
        for row in test_data1:
            self.assertEqual(self.calculator.subtract(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_addition(self):
        test_data1 = CsvReader('tests/Data/addition.csv').data
        for row in test_data1:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication(self):
        test_data = CsvReader('tests/Data/multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        test_data2 = CsvReader('tests/Data/division.csv').data
        for row in test_data2:
            self.assertEqual(self.calculator.divide(int(row['Value 1']), int(row['Value 2'])), round(float(row['Result'])))
            self.assertEqual(self.calculator.result, round(float(row['Result'])))

    def test_squares(self):
        test_data2 = CsvReader('tests/Data/square.csv').data
        for row in test_data2:
            self.assertEqual(self.calculator.square(int(row['Value 1'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_root(self):
        test_data2 = CsvReader('tests/Data/square_root.csv').data
        for row in test_data2:
            self.assertEqual(self.calculator.sq_root(int(row['Value 1'])), round(float(row['Result']), 8))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 8))

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
