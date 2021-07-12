from Calculator.Square_root import square_root
from Statistics_module.Variance import variance


def stddev(num):
    try:
        variance_float = variance(num)
        return round(square_root(variance_float), 5)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")