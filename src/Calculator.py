import math
from CsvReader import CsvReader


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c


def division(a, b):
    a = int(a)
    b = int(b)
    c = round(float(b / a))
    return c


def squares(a):
    a = int(a)
    b = int(a * a)
    return b


def square_root(a):
    a = int(a)
    b = math.sqrt(a)
    return round(float(b), 8)


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
        self.data = CsvReader(data_file)
        pass
