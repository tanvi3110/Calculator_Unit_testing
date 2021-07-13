import math
from Statistics_module.Variance import variance


def standard_deviation(std_deviation_list):
    try:
        dev = math.sqrt(variance(std_deviation_list))
        return dev
    except IndexError or ValueError:
        return None
