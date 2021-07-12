from Calculator.Squares import squares
from Calculator.Division import division
from Statistics_module.PopulationMean import population_mean


def variance(num):
    try:
        pop_mean = population_mean(num)
        num_values = len(num)
        x = 0
        for i in num:
            x = x + squares(i-pop_mean)
        return division(x, num_values)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")