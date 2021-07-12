from Calculator.Addition import addition
from Calculator.Division import division


def population_mean(num):
    try:
        num_values = len(num)
        total = sum(num)
        return division(total, num_values)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")