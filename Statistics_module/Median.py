from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition


def median(num):
    try:
        n = len(num)
        num.sort()
        median1 = num[n // 2]
        median2 = num[n // 2 - 1]
        result_median = addition(median1, median2)
        result_median2 = division(2, result_median)
        return result_median2
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")
