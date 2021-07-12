from Calculator.Addition import addition
from Calculator.Division import division
from Statistics_module.Getsample import getSample


def sample_mean(data, sample_size):
    try:
        total = 0
        sample = getSample(data, sample_size)
        num_value = len(sample)
        for num in sample:
            total = addition(total, num)
        return round(division(total, num_value), 8)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print ("Error: Check your data inputs")


#  check that get sample returns the proper number of samples
    # check that sample size is not 0
    # check that sample size is not larger than the population
    # https://realpython.com/python-exceptions/
# https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception



