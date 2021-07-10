from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Squares import squares
from Calculator.Square_root import square_root

from CsvReader import CsvReader


class Calculator:
    result = 0

    def __init__(self):
        pass

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = squares(a)
        return self.result

    def sq_root(self, a):
        self.result = square_root(a)
        return self.result


class CSVStats(Calculator):
    data = []

    def __init__(self, data_file):
        super().__init__()
        self.data = CsvReader.CsvReader(data_file)
