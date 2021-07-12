from Calculator.Addition import addition
from Calculator.Division import division
# from Statistics_module.Getsample import getSample


def sample_mean(mean_list):
    try:
        c = sum(mean_list) / len(mean_list)
        return c
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")


#  check that get sample returns the proper number of samples
    # check that sample size is not 0
    # check that sample size is not larger than the population
    # https://realpython.com/python-exceptions/
#  https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception



