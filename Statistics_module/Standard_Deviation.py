import math
from Statistics_module.Variance import variance


def standard_deviation(std_deviation_list):
    try:
        dev = math.sqrt(variance(std_deviation_list))
        return dev
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")
