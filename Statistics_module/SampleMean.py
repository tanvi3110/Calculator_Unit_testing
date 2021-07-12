from Calculator.Addition import addition
from Calculator.Calculator import Calculator
from Calculator.Division import division


class SampleMean(Calculator):

    def smean(self, mean_list):
        try:
            total = 0
            for num in mean_list:
                total = addition(total, num)
            return division(len(mean_list), total)
        except ZeroDivisionError:
            print("Error: Can't Divide by 0")
        except ValueError:
            print("Error: Check your data inputs")
